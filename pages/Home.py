import streamlit as st
import pandas as pd


if not st.session_state.get("logged_in", False):
    st.warning("Please Login First")
    st.stop()

with st.sidebar:

    st.title("🛒 AI Recommender")

    st.success("Logged In")

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.rerun()

st.set_page_config(layout="wide")

df = pd.read_csv("amazon_products_final.csv")

st.title("🛒 Product Explorer")

search = st.text_input("🔍 Search Products")

category = st.selectbox(
    "Select Category",
    ["All"] + sorted(df["main_category"].unique())
)

filtered = df.copy()

if category != "All":
    filtered = filtered[
        filtered["main_category"] == category
    ]

if search:
    filtered = filtered[
        filtered["name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]
st.divider()

st.subheader("🔥 Top Rated Products")

top_products = (
    df.sort_values(
        "ratings",
        ascending=False
    )
    .head(8)
)

cols = st.columns(4)

for idx, (_, row) in enumerate(
    top_products.iterrows()
):

    with cols[idx % 4]:

        try:
            st.image(
                row["image"],
                width=180
            )
        except:
            pass

        st.write(
            row["name"][:40]
        )

        st.write(
            f"⭐ {row['ratings']}"
        )    

st.write(f"### Products Found: {len(filtered)}")

products = filtered.head(24)

cols = st.columns(4)

for idx, (_, row) in enumerate(products.iterrows()):

    with cols[idx % 4]:

        try:
            st.image(
                row["image"],
                width=180
            )
        except:
            pass

        st.markdown(
            f"**{row['name'][:70]}**"
        )

        st.write(f"⭐ {row['ratings']}")

        st.write(
            f"₹{int(row['discount_price'])}"
        )

        st.caption(
            row["sub_category"]
        )