import streamlit as st
import pandas as pd
import os
import json
import random
from io import BytesIO

# Load or initialize data
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"challenges": [], "journal": []}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

data = load_data()



# Streamlit App
st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")
st.title("🚀 Growth Mindset Challenge!")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Challenge", "Quiz", "Journal & Reflection", "File Converter"])



# Home Page
if page == "Home":
    st.header("Welcome to the Growth Mindset Challenge!")
    st.write("A growth mindset is the belief that intelligence and abilities can be developed through dedication and hard work.")
    
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg")
    
    st.subheader("Why Growth Mindset Matters?")
    st.write("A growth mindset helps you embrace challenges, learn from criticism, and persist in the face of setbacks. It encourages continuous learning and resilience.")
    
    st.subheader("Benefits of a Growth Mindset")
    st.write("- **Embracing Challenges:** See difficulties as opportunities for growth.")
    st.write("- **Learning from Mistakes:** Understand that mistakes are part of the learning process.")
    st.write("- **Developing Resilience:** Stay committed to your goals despite obstacles.")
    st.write("- **Fostering Creativity:** Encourages innovative problem-solving skills.")
    
    st.subheader("How to Cultivate a Growth Mindset?")
    st.write("- **Set Learning Goals:** Focus on acquiring new skills instead of just results.")
    st.write("- **Practice Self-Reflection:** Regularly analyze your progress and areas for improvement.")
    st.write("- **Seek Constructive Feedback:** Use feedback to enhance your learning.")
    st.write("- **Stay Positive:** Keep an optimistic approach towards learning and growth.")
    
    st.subheader("Inspirational Quote")
    st.write("\"Success is not the result of talent alone, but of effort, persistence, and a willingness to learn.\" - Carol Dweck")



# Daily Challenge
elif page == "Daily Challenge":
    st.header("🌟 Today's Growth Mindset Challenge")
    
    st.write("Embracing a growth mindset means consistently challenging yourself to improve and learn. Each day, take on a new challenge to foster resilience and self-improvement.")
    
    challenges = [
        "Write down three things you learned today and how they can help you grow.",
        "Share a mistake you made recently, what you learned from it, and how you'll avoid it in the future.",
        "Set a clear and measurable goal for self-improvement this week. Outline steps to achieve it.",
        "Encourage someone else to adopt a growth mindset by sharing an inspiring story or helpful advice.",
        "Reflect on a difficult situation you faced and how adopting a growth mindset helped you overcome it.",
        "Read about a successful person who embodies a growth mindset and summarize key takeaways.",
        "Try something outside your comfort zone and document your experience and feelings."
    ]
    
    challenge = random.choice(challenges)
    st.subheader("✨ Your Challenge Today:")
    st.write(challenge)
    
    response = st.text_area("How will you complete this challenge? Share your thoughts and plan.")
    
    if st.button("Submit Response"):
        data["challenges"].append({"challenge": challenge, "response": response})
        save_data(data)
        st.success("🎉 Your response has been saved! Keep pushing yourself towards growth!")
    
    st.info("💡 Remember: Growth comes from stepping out of your comfort zone. Take this challenge seriously and embrace the process!")



# Quiz Section
elif page == "Quiz":
    st.header("🧠 Growth Mindset Quiz")
    quiz_questions = [
        {"question": "What is a key trait of a growth mindset?", "options": ["Avoiding challenges", "Embracing challenges", "Giving up easily"], "answer": "Embracing challenges"},
        {"question": "How should you view mistakes?", "options": ["As failures", "As learning opportunities", "As things to avoid"], "answer": "As learning opportunities"},
        {"question": "What is the best way to deal with setbacks?", "options": ["Give up", "Learn from them", "Ignore them"], "answer": "Learn from them"},
        {"question": "What is a good way to develop a growth mindset?", "options": ["Stick to what you know", "Try new challenges", "Avoid feedback"], "answer": "Try new challenges"},
        {"question": "How should you react to constructive criticism?", "options": ["Ignore it", "Use it to improve", "Take it personally"], "answer": "Use it to improve"},
        {"question": "Which of these is a characteristic of a fixed mindset?", "options": ["Believing abilities can grow", "Avoiding failure", "Seeking challenges"], "answer": "Avoiding failure"},
        {"question": "Why is persistence important in a growth mindset?", "options": ["It helps overcome obstacles", "It guarantees success", "It is unnecessary"], "answer": "It helps overcome obstacles"}
    ]
    
    score = 0
    for q in quiz_questions:
        st.write(q["question"])
        option = st.radio("Choose an answer:", q["options"], key=q["question"])
        if option == q["answer"]:
            score += 1
    
    if st.button("Submit Quiz"):
        st.write(f"Your score: {score}/{len(quiz_questions)}")



# Journal & Reflection
elif page == "Journal & Reflection":
    st.header("📖 Personal Journal")
    st.subheader("Daily Reflection")
    st.write("Take a moment to reflect on your growth mindset journey.")
    journal_entry = st.text_area("Write about your experiences, challenges, and successes today:")
    if st.button("Save Entry"):
        if journal_entry.strip():
            data["journal"].append(journal_entry)
            save_data(data)
            st.success("Your journal entry has been saved!")
        else:
            st.error("Please write something before saving.")

    st.subheader("📜 Past Entries")
    if data["journal"]:
        for i, entry in enumerate(reversed(data["journal"])):
            st.write(f"**Entry {len(data['journal']) - i}:** {entry}")
    else:
        st.write("No journal entries yet. Start writing today!")


# File Converter
elif page == "File Converter":
    st.header("📂 CSV & Excel File Converter")
    upload_Files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)
    if upload_Files:
        for file in upload_Files:
            file_extension = os.path.splitext(file.name)[-1].lower()
            if file_extension == ".csv":
                df = pd.read_csv(file)
            elif file_extension == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported File type:{file_extension}")
                continue
            st.write(f"**File Name**: {file.name}")
            st.write(f"**File Size**: {file.size/1024} KB")
            st.dataframe(df.head())
            if st.checkbox(f"Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_extension, ".csv")
                    mime_type = "text/csv"
                else:
                    df.to_excel(buffer, index=False, engine='openpyxl')  # Save as Excel using openpyxl
                    file_name = file.name.replace(file_extension, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)
                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )
st.success("🎉All features loaded successfully! Enjoy your Growth Mindset journey!")
