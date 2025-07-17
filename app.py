import streamlit as st
from inference import chat_inference

st.title("Bot chat Sederhana dengan Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
prompt = st.chat_input("Ketik pesan disini")
if prompt:
    response = chat_inference(prompt)
    
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({
            "role": "user", "content": prompt
        })
        
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({
            "role": "assistant", "content": prompt
        })



# prompt = st.chat_input("Ketik peasn disini")
# if prompt:
#     response = chat_inference(prompt)
#     with st.chat_message("assistant"):
#         st.markdown(response)