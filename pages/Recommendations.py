import streamlit as st
import pandas as pd
from recommender import ProductRecommender


if not st.session_state.get("logged_in", False):
    st.warning("Please Login First")
    st.stop()

with st.sidebar:

    st.title("🛒 AI Recommender")

    st.success("Logged In")

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.rerun()
        
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "history" not in st.session_state:
    st.session_state.history = []

if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

@st.cache_resource
def load_model():
    return ProductRecommender("amazon_products_final.csv")

model = load_model()

df = pd.read_csv("amazon_products_final.csv")

st.title("🎯 Smart Recommendations")

st.write("❤️ Wishlist Items:", len(st.session_state.wishlist))

product = st.selectbox(
    "Select Product",
    df["name"]
)

# Generate recommendations
if st.button("Get Recommendations"):

    st.session_state.history.append(product)

    st.session_state.recommendations = model.recommend(
        product,
        top_n=8
    )

# Display recommendations (outside button block)
if st.session_state.recommendations is not None:

    recommendations = st.session_state.recommendations

    cols = st.columns(4)

    for idx, (_, row) in enumerate(recommendations.iterrows()):

        with cols[idx % 4]:

            try:
                st.image(
                    row["image"],
                    width=180
                )
            except:
                st.write("No Image")

            st.markdown(
                f"**{row['name'][:60]}**"
            )

            st.write(
                f"⭐ {row['ratings']}"
            )

            st.write(
                f"₹{int(row['discount_price'])}"
            )

            with st.expander("View Details"):
                st.write(
                    "Category:",
                    row["main_category"]
                      )
                st.write(
                     "Sub Category:",
                     row["sub_category"]
                       )
                st.write(
                    "Rating:",
                    row["ratings"]
                    )
                st.write(
                    "Price:",
                    row["discount_price"]
                    )
                st.write(
                    "Original Price:",
                    row["actual_price"]
                    )

            if st.button(
                "❤️ Add",
                key=f"wish_{idx}"
            ):

                if row["name"] not in st.session_state.wishlist:

                    st.session_state.wishlist.append(
                        row["name"]
                    )

                    st.success("Added to Wishlist!")