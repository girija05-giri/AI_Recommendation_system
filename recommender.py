import pandas as pd


class ProductRecommender:

    def __init__(self, csv_path):

        self.df = pd.read_csv(csv_path)

        self.df.fillna("", inplace=True)

        self.df["discount_price"] = pd.to_numeric(
            self.df["discount_price"],
            errors="coerce"
        )

        self.df["ratings"] = pd.to_numeric(
            self.df["ratings"],
            errors="coerce"
        )

    def recommend(self, product_name, top_n=8):

        product = self.df[
            self.df["name"] == product_name
        ]

        if len(product) == 0:
            return pd.DataFrame()

        product = product.iloc[0]

        subcat = product["sub_category"]
        price = product["discount_price"]

        recommendations = self.df[
            self.df["sub_category"] == subcat
        ].copy()

        recommendations = recommendations[
            recommendations["name"] != product_name
        ]

        recommendations["price_diff"] = (
            recommendations["discount_price"] - price
        ).abs()

        recommendations = recommendations.sort_values(
            by=["price_diff", "ratings"],
            ascending=[True, False]
        )

        return recommendations.head(top_n)