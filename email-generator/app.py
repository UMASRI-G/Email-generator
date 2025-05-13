import streamlit as st
from email_generator import generate_email

st.title("✉️ AI Email Generator")

# Input fields for subject and tone
subject = st.text_input("Subject of the email", placeholder="Enter subject here")
tone = st.selectbox("Select Tone", ["Formal", "Friendly"])

# Generate the email when the button is clicked
if st.button("Generate Email"):
    if subject:
        with st.spinner("Generating email..."):
            email = generate_email(subject, tone)
            st.subheader("📧 Generated Email:")
            st.markdown(email)
    else:
        st.warning("Please enter a subject.")
