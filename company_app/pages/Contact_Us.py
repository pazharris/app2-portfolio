import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Us")
df = pandas.read_csv("topics.csv")
with st.form("email_form"):
    user_email = st.text_input("Your email address")
    option = st.selectbox("What do you want to discuss?",
                          df["topic"])

    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}\

Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")