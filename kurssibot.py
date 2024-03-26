from openai import OpenAI
import streamlit as st
from prompts import *

client = OpenAI(api_key=st.secrets["apikey"])

st.title("KurssiBot")

st.session_state.setdefault("openai_model", "gpt-3.5-turbo-1106")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt_content2}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Kysy minulta neuvoa")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

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
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})


