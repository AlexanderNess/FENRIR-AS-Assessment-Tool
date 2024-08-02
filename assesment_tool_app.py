import streamlit as st

st.title("Norwegian Investment Readiness Assessment Tool")

st.write("Welcome to the Norwegian Investment Readiness Assessment Tool. Answer the questions below to assess your readiness for investing in Norway.")

# Sample questions
questions = {
    "Experience in investing": ["None", "Beginner", "Intermediate", "Advanced"],
    "Knowledge of Norwegian market": ["None", "Basic", "Moderate", "Extensive"],
    "Capital available for investment": [0, 50000, 100000, 200000, 500000],
    "Risk tolerance": ["Low", "Moderate", "High", "Very High"]
}

scores = {}

# Questionnaire loop
for question, options in questions.items():
    if isinstance(options[0], str):
        scores[question] = st.radio(question, options)
    else:
        scores[question] = st.slider(question, min_value=options[0], max_value=options[-1], value=options[0])

# Scoring logic
score_mapping = {
    "None": 0,
    "Basic": 1,
    "Beginner": 1,
    "Low": 1,
    "Moderate": 2,
    "Intermediate": 2,
    "High": 3,
    "Extensive": 3,
    "Advanced": 3,
    "Very High": 4
}

total_score = 0

# Calculate total score
for key, value in scores.items():
    total_score += score_mapping.get(value, 0)

# Output summary
st.write(f"Your total readiness score is: {total_score}")

if total_score < 5:
    st.write("Based on your responses, it seems you might need more preparation before investing in Norway. Consider gaining more knowledge about the market and clarifying your investment goals.")
elif 5 <= total_score < 8:
    st.write("You have a moderate level of readiness. Some aspects might need more attention, but you are on the right track.")
else:
    st.write("You are well-prepared for investing in Norway. Consider discussing specific opportunities with a financial advisor or investment professional.")

# Footer
st.write("For more resources, visit [FENRIR AS](https://www.fenrir.fund/).")

