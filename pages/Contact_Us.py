import streamlit as st

from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
    button= st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message, user_email)
        st.info("Your email was send successfully")