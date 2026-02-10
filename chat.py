import streamlit as st
from groq import Groq

# Create Groq client using Streamlit Secrets
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

st.set_page_config(page_title="Groq Chat", page_icon="💬")

st.title("💬 Groq Chat Assistant")
st.caption("Fast LLMs with memory using Streamlit + Groq")

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Groq API with full conversation (memory enabled)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages,
    )

    assistant_reply = response.choices[0].message.content

    # Store assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
