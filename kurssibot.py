from openai import OpenAI
import streamlit as st
from prompts import *

client = OpenAI(api_key=st.secrets["apikey"])

st.title("KurssiBot")

# Initialize the openai_model in session_state with a default value
st.session_state.setdefault("openai_model", "gpt-3.5-turbo-1106")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Kysy minulta neuvoa"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Check and trim chat history if necessary
    if len(st.session_state.messages) > MAX_CHAT_HISTORY:
        st.session_state.messages = st.session_state.messages[-MAX_CHAT_HISTORY:]

    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner('puppugeneraattori aktivoitu'):
            for response in client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=st.session_state.messages,
                stream=True):
                if response.choices[0].delta.role != "system":
                    content = response.choices[0].delta.content
                    if content is not None:
                        full_response += content
            message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
    
    # Append assistant's response
    st.session_state.messages.append({"role": "assistant", "content": full_response})

