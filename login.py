import streamlit as st
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
st.set_page_config(
    page_title="AI Product Recommendation System",
    page_icon="🛒",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🛒 AI Product Recommendation System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.rerun()

    st.stop()

st.title("🛒 AI Product Recommendation System")
st.success("Login Successful!")

st.write("Use the sidebar to navigate.")