import streamlit as st
from pint import UnitRegistry
import random
import time
from collections import deque

# Initialize Unit Registry
ureg = UnitRegistry()

# Conversion History (Session State)
if "conversion_history" not in st.session_state:
    st.session_state.conversion_history = deque(maxlen=5)

# Unit Categories with Icons
unit_categories = {
    "📏 Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "⚖️ Mass": ["gram", "kilogram", "pound", "ounce", "tonne"],
    "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    "📐 Area": ["square meter", "hectare", "acre", "square mile"],
    "💾 Digital Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte"],
    "⚡ Energy": ["joule", "calorie", "kilowatt-hour"],
    "🔄 Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "⏳ Time": ["second", "minute", "hour", "day"],
    "🎛️ Pressure": ["pascal", "bar", "psi"],
    "📊 Volume": ["liter", "milliliter", "gallon", "cup", "fluid ounce"],
}

# Fun Facts
fun_facts = [
    "Did you know? 1 light-year equals 9.46 trillion km!",
    "A joule is named after James Prescott Joule, who studied energy!",
    "Kelvin is the absolute temperature scale used in science!",
    "1 mile is equal to 1.609 kilometers!",
    "The bit is the smallest unit of digital storage!",
]

# Streamlit UI Setup
st.set_page_config(page_title="Unit Converter 🔄", layout="wide")
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Select a section", ["Unit Converter", "Guess the Conversion", "Speed Challenge", "Conversion History"])

# Conversion Function
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        formatted_result = "{:.0f}".format(result.magnitude) if result.magnitude.is_integer() else "{:.4f}".format(result.magnitude).rstrip('0').rstrip('.')
        return result.magnitude, f"{value} {from_unit} = {formatted_result} {to_unit}"
    except Exception as e:
        return None, str(e)

# Unit Converter Page
if page == "Unit Converter":
    st.title("🔄 Unit Converter")
    
    # Full-width Category Selection
    category = st.selectbox("📌 Select a Category", list(unit_categories.keys()))
    
    # Two Columns for 'Convert From' and 'Convert To'
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Convert From:", unit_categories[category])
    with col2:
        to_unit = st.selectbox("Convert To:", unit_categories[category])
    
    # Full-width for Value Input
    value = st.number_input("🔢 Enter Value:", min_value=0.0, format="%.10g")

    if st.button("Convert"):
        converted_value, result_text = convert_units(value, from_unit, to_unit)
        if converted_value is not None:
            st.success(result_text)
            st.session_state.conversion_history.appendleft(result_text)
            st.info(random.choice(fun_facts))
        else:
            st.error("Invalid conversion! Check units.")


# Guess the Conversion Game
elif page == "Guess the Conversion":
    st.title("🎯 Guess the Conversion!")
    category = random.choice(list(unit_categories.keys()))
    units = unit_categories[category]
    from_unit, to_unit = random.sample(units, 2)
    value = random.randint(1, 100)
    correct_answer, _ = convert_units(value, from_unit, to_unit)
    
    if correct_answer is not None:
        user_guess = st.number_input(f"Convert {value} {from_unit} to {to_unit}", key=f"guess_{random.randint(1000,9999)}", format="%.10g")
        if st.button("Submit Guess"):
            if abs(user_guess - correct_answer) < 0.1:
                st.success("🎉 Correct! Well done!")
            else:
                st.error(f"❌ The correct answer is {correct_answer:.4f} {to_unit}")

# Speed Challenge Game
elif page == "Speed Challenge":
    st.title("⏳ Speed Challenge: Convert as many as possible in 30 seconds!")
    
    if "challenge_active" not in st.session_state:
        st.session_state.challenge_active = False
        st.session_state.score = 0
        st.session_state.start_time = None
        st.session_state.current_question = None

    if not st.session_state.challenge_active:
        if st.button("Start Challenge"):
            st.session_state.challenge_active = True
            st.session_state.score = 0
            st.session_state.start_time = time.time()
            st.session_state.current_question = {}
    
    if st.session_state.challenge_active:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, 30 - elapsed_time)
        st.info(f"⏳ Time Left: {remaining_time:.1f} seconds")

        if remaining_time > 0:
            if not st.session_state.current_question:
                category = random.choice(list(unit_categories.keys()))
                from_unit, to_unit = random.sample(unit_categories[category], 2)
                value = random.randint(1, 100)
                correct_answer, _ = convert_units(value, from_unit, to_unit)
                st.session_state.current_question = {
                    "category": category,
                    "from_unit": from_unit,
                    "to_unit": to_unit,
                    "value": value,
                    "correct_answer": correct_answer
                }

            question = st.session_state.current_question
            user_guess = st.number_input(
                f"Convert {question['value']} {question['from_unit']} to {question['to_unit']}",
                key="speed_challenge_input",
                format="%.10g"
            )

            if st.button("Submit Answer"):
                if abs(user_guess - question["correct_answer"]) < 0.1:
                    st.success("🎉 Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Correct answer: {question['correct_answer']:.4f}")
                st.session_state.current_question = {}
        else:
            st.session_state.challenge_active = False
            st.success(f"🏆 Time's up! Your final score: {st.session_state.score}")
            st.session_state.current_question = None

elif page == "Conversion History":
    st.title("📜 Conversion History")
    if st.session_state.conversion_history:
        for entry in list(st.session_state.conversion_history):
            st.write(entry)
    else:
        st.info("No conversions yet. Start converting!")

