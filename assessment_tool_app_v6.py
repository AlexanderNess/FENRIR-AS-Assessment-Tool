import streamlit as st

# Title and Introduction
st.title("Norwegian Investment Readiness Assessment Tool for FENRIR AS")
st.write("""
Welcome to FENRIR's Investment Readiness Assessment Tool. This tool is designed to evaluate your suitability as an investor in compliance with Norwegian AIF regulations. Please answer the following questions accurately.
""")

# Function to render questions with slightly larger text
def larger_text(text):
    st.markdown(f"<p style='font-size: 1.05em; margin-bottom: 0;'>{text}</p>", unsafe_allow_html=True)

# Question 1: Investor Eligibility
st.subheader("1. Investor Eligibility")
larger_text("Are you classified as a professional investor under the Norwegian Alternative Investment Fund Act?")
eligibility = st.radio(
    "",
    options=["Please select an option", "Yes", "No", "Unsure"]
)

# Question 2: Investment Experience
st.subheader("2. Investment Experience")
larger_text("Do you have prior experience investing in alternative investment funds or similar financial instruments?")
experience = st.radio(
    "",
    options=["Please select an option", "Yes, extensive", "Yes, some", "No, none"]
)

# Question 3: Understanding of Investment Risks
st.subheader("3. Understanding of Investment Risks")
larger_text("Are you aware that investments in an AIF can involve significant risks, including the potential loss of capital?")
risk_acknowledgement = st.radio(
    "",
    options=["Please select an option", "Yes", "No"]
)

# Question 4: Source of Funds (AML Compliance)
st.subheader("4. Source of Funds")
larger_text("Please describe the source of funds you intend to use for this investment (e.g., savings, income, sale of assets).")
source_of_funds = st.text_input("")

# Question 5: Disclosure Agreement
st.subheader("5. Disclosure Agreement")
larger_text("I acknowledge that I have read and understood the information regarding the risks and nature of the investments offered by FENRIR AS, as provided in the AIF's offering documents.")
disclosure = st.checkbox("")

# Submission and Evaluation
st.subheader("Assessment Summary")
if st.button("Submit Assessment"):
    if eligibility != "Please select an option" and experience != "Please select an option" and risk_acknowledgement != "Please select an option" and disclosure:
        if eligibility == "Yes" and experience != "No, none" and risk_acknowledgement == "Yes":
            st.write("Based on your responses, you appear to meet the basic requirements for investment in FENRIR AS. Our team will review your details and contact you for further discussions.")
        else:
            st.write("Based on your responses, it appears that you may not meet the regulatory requirements for investing in FENRIR AS. We recommend consulting with a financial advisor for further clarification.")
    else:
        st.write("Please ensure all questions are answered before submitting.")

st.write("For more information, visit [FENRIR's website](https://www.fenrir.fund/).")
import streamlit as st

# Title and Introduction
st.title("Norwegian Investment Readiness Assessment Tool for FENRIR AS")
st.write("""
Welcome to FENRIR's Investment Readiness Assessment Tool. This tool is designed to evaluate your suitability as an investor in compliance with Norwegian AIF regulations. Please answer the following questions accurately.
""")

# Function to render questions with slightly larger text
def larger_text(text):
    st.markdown(f"<p style='font-size: 1.05em; margin-bottom: 0;'>{text}</p>", unsafe_allow_html=True)

# Question 1: Investor Eligibility
st.subheader("1. Investor Eligibility")
larger_text("Are you classified as a professional investor under the Norwegian Alternative Investment Fund Act?")
eligibility = st.radio(
    "",
    options=["Please select an option", "Yes", "No", "Unsure"]
)

# Question 2: Investment Experience
st.subheader("2. Investment Experience")
larger_text("Do you have prior experience investing in alternative investment funds or similar financial instruments?")
experience = st.radio(
    "",
    options=["Please select an option", "Yes, extensive", "Yes, some", "No, none"]
)

# Question 3: Understanding of Investment Risks
st.subheader("3. Understanding of Investment Risks")
larger_text("Are you aware that investments in an AIF can involve significant risks, including the potential loss of capital?")
risk_acknowledgement = st.radio(
    "",
    options=["Please select an option", "Yes", "No"]
)

# Question 4: Source of Funds (AML Compliance)
st.subheader("4. Source of Funds")
larger_text("Please describe the source of funds you intend to use for this investment (e.g., savings, income, sale of assets).")
source_of_funds = st.text_input("")

# Question 5: Disclosure Agreement
st.subheader("5. Disclosure Agreement")
larger_text("I acknowledge that I have read and understood the information regarding the risks and nature of the investments offered by FENRIR AS, as provided in the AIF's offering documents.")
disclosure = st.checkbox("")

# Submission and Evaluation
st.subheader("Assessment Summary")
if st.button("Submit Assessment"):
    if eligibility != "Please select an option" and experience != "Please select an option" and risk_acknowledgement != "Please select an option" and disclosure:
        if eligibility == "Yes" and experience != "No, none" and risk_acknowledgement == "Yes":
            st.write("Based on your responses, you appear to meet the basic requirements for investment in FENRIR AS. Our team will review your details and contact you for further discussions.")
        else:
            st.write("Based on your responses, it appears that you may not meet the regulatory requirements for investing in FENRIR AS. We recommend consulting with a financial advisor for further clarification.")
    else:
        st.write("Please ensure all questions are answered before submitting.")

st.write("For more information, visit [FENRIR's website](https://www.fenrir.fund/).")
