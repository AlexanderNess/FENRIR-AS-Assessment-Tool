import streamlit as st

# Title and Introduction
st.title("Norwegian Investment Readiness Assessment Tool for FENRIR AS")
st.write("""
Welcome to the FENRIR AS Investment Readiness Assessment Tool. This tool is designed to evaluate your suitability as an investor in compliance with Norwegian AIF regulations. Please answer the following questions accurately.
""")

# Question 1: Investor Eligibility
st.subheader("1. Investor Eligibility")
eligibility = st.radio(
    "Are you classified as a professional investor under the Norwegian Alternative Investment Fund Act?",
    ("Yes", "No", "Unsure")
)

# Question 2: Investment Experience
st.subheader("2. Investment Experience")
experience = st.radio(
    "Do you have prior experience investing in alternative investment funds or similar financial instruments?",
    ("Yes, extensive", "Yes, some", "No, none")
)

# Question 3: Understanding of Investment Risks
st.subheader("3. Understanding of Investment Risks")
risk_acknowledgement = st.radio(
    "Are you aware that investments in an AIF can involve significant risks, including the potential loss of capital?",
    ("Yes", "No")
)

# Question 4: Source of Funds (AML Compliance)
st.subheader("4. Source of Funds")
source_of_funds = st.text_input(
    "Please describe the source of funds you intend to use for this investment (e.g., savings, income, sale of assets)."
)

# Question 5: Disclosure Agreement
st.subheader("5. Disclosure Agreement")
disclosure = st.checkbox(
    "I acknowledge that I have read and understood the information regarding the risks and nature of the investments offered by FENRIR AS, as provided in the AIF's offering documents."
)

# Submission and Evaluation
st.subheader("Assessment Summary")
if st.button("Submit Assessment"):
    if eligibility == "Yes" and experience != "No, none" and risk_acknowledgement == "Yes" and disclosure:
        st.write("Based on your responses, you appear to meet the basic requirements for investment in FENRIR AS. Our team will review your details and contact you for further discussions.")
    else:
        st.write("Based on your responses, it appears that you may not meet the regulatory requirements for investing in FENRIR AS. We recommend consulting with a financial advisor for further clarification.")

st.write("For more information, visit [FENRIR AS](https://www.fenrir.fund/).")
