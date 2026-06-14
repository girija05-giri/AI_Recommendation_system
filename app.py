import streamlit as st

st.set_page_config(
    page_title="AI Product Recommendation System",
    page_icon="🛒",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in:

    st.title("🛒 AI Product Recommendation System")

    st.markdown("### Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username and password:

            st.session_state.logged_in = True
            st.session_state.username = username

            st.rerun()

    st.stop()

st.title("🏠 Welcome")

st.success(
    f"Welcome {st.session_state.username} 👋"
)

st.markdown("""
### Features

- 🔍 Product Search
- 🎯 Smart Recommendations
- ❤️ Wishlist
- 🕒 History
- 📊 Dashboard Analytics

Use the sidebar to navigate.
""")

if st.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.rerun()