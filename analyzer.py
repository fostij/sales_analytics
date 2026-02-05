import pandas as pd
import numpy as np
from utils import parse_date, to_float



class SalesAnalyser:
    def __init__(self, path="data/sales_data.csv"):
        self.path = path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.path)

    def clean_data(self):
        df = self.df.copy()

        df = df.drop_duplicates()
        df["order_date"] = parse_date(df["order_date"])
        df["order_amount"] = to_float(df["order_amount"])
        df["status"] = df["status"].fillna("unknown")

        df = df.dropna(subset=["order_date", "order_amount"])

        self.df = df
        df.to_csv("data/sales_clean.csv", index=False)

    def analytics(self):
        df = self.df

        results = {}
        results["total_revenue"] = df["order_amount"].sum()
        results["aov"] = df["order_amount"].mean()
        results["customer_count"] = df["customer_id"].nunique()
        results["revenue_by_category"] = (
            df.groupby("product_category")["order_amount"].sum()
        )
        results["top_customers"] = (
            df.groupby("customer_id")["order_amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        results["status_distribution"] = df["status"].value_counts(normalize=True)

        return results