import streamlit as st
from openai import OpenAI
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="TripSage – AI Travel Concierge",
    page_icon="✈️",
    layout="centered"
)
st.title("✈️ TripSage – AI Travel Concierge")
st.write("Plan smarter. Travel better. 💙")
# 🔐 Paste your Groq API key here
GROQ_API_KEY = "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"
# Groq OpenAI-compatible client
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)
# ---------------- SESSION MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI travel assistant."}
    ]
# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Ask about flights, hotels, itineraries...")
if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    try:
        with st.spinner("Planning your trip... ✨"):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # ✅ Current supported Groq model
                messages=st.session_state.messages,
                temperature=0.7,
            )
        reply = response.choices[0].message.content
        # Save assistant reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.error(f"Error: {e}")
        