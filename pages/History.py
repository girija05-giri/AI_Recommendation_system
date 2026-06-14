import streamlit as st

if not st.session_state.get("logged_in", False):
    st.stop()

st.title("🕒 Search History")

if "history" not in st.session_state:
    st.session_state.history = []

if len(st.session_state.history) == 0:

    st.info("No history available")

else:

    for item in reversed(
        st.session_state.history
    ):

        st.write("🔹", item)