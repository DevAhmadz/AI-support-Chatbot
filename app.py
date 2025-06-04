import streamlit as st
from chatbot import ask_question

st.title("AI IT support Chatbot")
query = st.text_input("Ask a question related to IT support or onboarding")

if query:
    response = ask_question(query)
    st.write("**Answer!", response)