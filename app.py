import streamlit as st
from groq import Groq

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Groq Chat",
    page_icon="⚡",
    layout="centered"
)

# ---------------- API KEY ----------------
# ❗ Replace with YOUR NEW key locally
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.user {
    background: #4f46e5;
    color: white;
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
    text-align: right;
}
.bot {
    background: #1f2937;
    color: #e5e7eb;
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Groq Chatbot")

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['content']}</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()

