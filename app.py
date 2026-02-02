import streamlit as st
from groq import Groq
import os

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Groq Chat",
    page_icon="⚡",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.chat-container {
    max-width: 700px;
    margin: auto;
}
.user-msg {
    background: linear-gradient(135deg, #4f46e5, #6366f1);
    color: white;
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
    text-align: right;
}
.bot-msg {
    background: #1f2937;
    color: #e5e7eb;
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
}
.header {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}
.sub {
    text-align: center;
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='header'>⚡ Groq AI Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Powered by LLaMA 3</div>", unsafe_allow_html=True)
st.divider()

# ---------------- API KEY ----------------
groq_api_key = os.environ.get("GROQ_API_KEY")

if not groq_api_key:
    st.error("❌ GROQ_API_KEY environment variable not set")
    st.stop()

client = Groq(api_key=groq_api_key)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CHAT DISPLAY ----------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    st.rerun()

# ---------------- FOOTER ----------------
st.divider()
st.caption("Built with Streamlit + Groq ⚡")
