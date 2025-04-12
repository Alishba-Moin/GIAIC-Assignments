import streamlit as st
import json
import os
import time
import base64
from typing import Optional, Dict, List, Any
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# ---------- Constants ----------
DATA_FILE: str = "secure_data.json"
MAX_ATTEMPTS: int = 3
LOCKOUT_DURATION: int = 60  # in seconds

# ---------- Initialize Session Variables ----------
for key in ["user_data", "login_attempts", "lockout_until", "logged_in_user"]:
    if key not in st.session_state:
        if key == "user_data":
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as file:
                    st.session_state[key] = json.load(file)
            else:
                st.session_state[key] = {}
        else:
            st.session_state[key] = {} if key != "logged_in_user" else None

# ---------- Helper Functions ----------

# Save all users to JSON file
def save_user_data() -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(st.session_state.user_data, f, indent=2)

# Create encryption key from password and salt
def get_key(password: str, salt: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Encrypt message
def encrypt(msg: str, password: str, salt: str) -> str:
    key: bytes = get_key(password, salt)
    fernet = Fernet(key)
    return fernet.encrypt(msg.encode()).decode()

# Decrypt message
def decrypt(token: str, password: str, salt: str) -> Optional[str]:
    try:
        key: bytes = get_key(password, salt)
        fernet = Fernet(key)
        return fernet.decrypt(token.encode()).decode()
    except Exception:
        return None

# Check login by decrypting any one message
def login(username: str, password: str) -> bool:
    if username not in st.session_state.user_data:
        return False

    for item in st.session_state.user_data[username]:
        if decrypt(item["message"], password, item["salt"]):
            st.session_state.logged_in_user = username
            st.session_state.login_attempts[username] = 0
            return True
    return False

# ---------- UI ----------
st.title("🔐 Simple Secure Notes App")

choice = ["Home", "Register", "Login", "Encrypt", "Decrypt", "Logout"]
menu = st.sidebar.selectbox("Choose An Action", choice)

# ---------- Home ----------
if menu == "Home":
    st.write("👋 Welcome! This app lets you encrypt your secret messages. Login to continue.")

# ---------- Register ----------
elif menu == "Register":
    username: str = st.text_input("New Username:")
    password: str = st.text_input("New Password:", type="password")

    if st.button("Register"):
        if username in st.session_state.user_data:
            st.warning("Username already exists!")
        else:
            salt: str = os.urandom(16).hex()
            encrypted: str = encrypt("Welcome message!", password, salt)
            st.session_state.user_data[username] = [{"message": encrypted, "salt": salt}]
            save_user_data()
            st.success("Registered successfully!")

# ---------- Login ----------
elif menu == "Login":
    username: str = st.text_input("Username:")
    password: str = st.text_input("Password:", type="password")

    now: float = time.time()
    is_locked: bool = username in st.session_state.lockout_until and now < st.session_state.lockout_until[username]

    if is_locked:
        wait: int = int(st.session_state.lockout_until[username] - now)
        st.error(f"Locked. Try again in {wait} seconds.")

    elif st.button("Login"):
        if login(username, password):
            st.success("Logged in successfully!")
        else:
            attempts: int = st.session_state.login_attempts.get(username, 0) + 1
            st.session_state.login_attempts[username] = attempts

            if attempts >= MAX_ATTEMPTS:
                st.session_state.lockout_until[username] = now + LOCKOUT_DURATION
                st.session_state.login_attempts[username] = 0
                st.warning("Too many attempts. Locked for 1 minute.")
            else:
                st.error(f"Wrong password. {MAX_ATTEMPTS - attempts} tries left.")

# ---------- Encrypt ----------
elif menu == "Encrypt":
    if not st.session_state.logged_in_user:
        st.warning("Login first to encrypt messages.")
    else:
        msg: str = st.text_area("Enter message:")
        password: str = st.text_input("Your password:", type="password")

        if st.button("Encrypt"):
            salt: str = os.urandom(16).hex()
            encrypted: str = encrypt(msg, password, salt)
            user: str = st.session_state.logged_in_user
            st.session_state.user_data[user].append({"message": encrypted, "salt": salt})
            save_user_data()
            st.success("Message saved securely.")
            st.code(encrypted)

# ---------- Decrypt ----------
elif menu == "Decrypt":
    if not st.session_state.logged_in_user:
        st.warning("Login first to decrypt messages.")
    else:
        encrypted: str = st.text_area("Paste encrypted message:")
        password: str = st.text_input("Your password:", type="password")

        if st.button("Decrypt"):
            user: str = st.session_state.logged_in_user
            for item in st.session_state.user_data[user]:
                result: Optional[str] = decrypt(encrypted, password, item["salt"])
                if result:
                    st.success("Decrypted message:")
                    st.code(result)
                    break
            else:
                st.error("Could not decrypt. Wrong password or message.")

# ---------- Logout ----------
elif menu == "Logout":
    st.session_state.logged_in_user = None
    st.success("Logged out successfully.")
