import streamlit as st

name = st.header("Happy Birthday Anand Bhai...")

messages = ["🎉 Happy Birthday!", "🎂 May your day be filled with bug-free code", "🎂 May your day be filled with seamless deployments", "Here’s to another year of pushing boundaries and debugging life’s challenges!"]

st.write(f"Anand Bhai! Happy birthday to you...")

if 'message_index' not in st.session_state:
    st.session_state.message_index = 0

if st.session_state.message_index < len(messages):
    if st.button("Click me"):
        st.session_state.message_index += 1
        st.write(f"{messages[st.session_state.message_index - 1]}")
else:
    st.write("Keep coding your dreams into reality! 💻✨")
    st.button("Click me", disabled=True)

st.balloons()