
import streamlit as st

if not st.session_state.get("logged_in", False):
    st.stop()

st.title("❤️ Wishlist")

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if len(st.session_state.wishlist) == 0:

    st.info("Wishlist Empty")

else:

    for item in st.session_state.wishlist:

        st.write("✅", item)

if st.button("Clear Wishlist"):

    st.session_state.wishlist = []

    st.rerun()