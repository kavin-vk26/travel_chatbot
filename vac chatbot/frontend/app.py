# frontend/app.py
import streamlit as st
import requests
import uuid

st.set_page_config(page_title="Travel Advisor Chatbot", page_icon="🌏")

st.title("🌏 Travel Advisor Chatbot")
st.write("Let's plan your perfect trip! ✈️")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Unique ID for each user session
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"user_message": user_input, "user_id": st.session_state.user_id}
    ).json()
    
    st.session_state.messages.append({"role": "bot", "text": response["bot_response"]})

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**Bot:** {msg['text']}")
