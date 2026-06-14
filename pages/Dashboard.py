import streamlit as st
import pandas as pd
import plotly.express as px


if not st.session_state.get("logged_in", False):
    st.warning("Please Login First")
    st.stop()
with st.sidebar:

    st.title("🛒 AI Recommender")

    st.success("Logged In")

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.rerun()    

df = pd.read_csv(
    "amazon_products_final.csv"
)
st.subheader(
    "Products By Category"
)

category_count = (
    df["main_category"]
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=category_count.index,
    y=category_count.values
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader(
    "Ratings Distribution"
)

fig2 = px.histogram(
    df,
    x="ratings"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

