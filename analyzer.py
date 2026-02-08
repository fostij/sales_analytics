import pandas as pd
from utils import parse_date, to_float
import matplotlib.pyplot as plt

"""
analyzer.py

Contains the SalesAnalyzer class, which is responsible for:
- loading raw data
- cleaning and validating datasets
- performing analytical computations
- generating reports and visualizations

This module encapsulates all data-related logic.
"""



class SalesAnalyser:
    """
    Central class responsible for sales data analysis.
    """
    def __init__(self, path="data/sales_data.csv"):
        self.path = path
        self.df = None

    def load_data(self):
        """
        Load raw sales data from CSV into a DataFrame.
        """
        self.df = pd.read_csv(self.path)

    def clean_data(self):
        """
        Clean and preprocess the dataset
        - remove duplicates
        - standardize data types
        - handle missing values
        - export cleaned dataset
        """
        df = self.df.copy()

        df = df.drop_duplicates()
        df["order_date"] = parse_date(df["order_date"])
        df["order_amount"] = to_float(df["order_amount"])
        df["status"] = df["status"].fillna("unknown")

        # Remove invalid rows after conversion
        df = df.dropna(subset=["order_date", "order_amount"])

        self.df = df
        df.to_csv("data/sales_clean.csv", index=False)

    def analytics(self):
        """
       Compute key business metrics using pandas aggregation.
        """
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
    
    def create_visualizations(self):
        """
        Create and export required visualizations using matplotlib.
        """
        df = self.df

        # 1. Revenue by category
        df.groupby("product_category")["order_amount"].sum().plot(
            kind="bar", figsize=(8, 5), title="Revenue by Category"
        )
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.savefig("output/figures/revenue_by_category.png")
        plt.clf()

        # 2. Monthly revenue trend
        df.set_index("order_date").resample("ME")["order_amount"].sum().plot(
            figsize=(8, 5), title="Monthly Revenue Trend"
        )
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.savefig("output/figures/monthly_trend.png")
        plt.clf()

        # 3. Order value distribution
        df["order_amount"].plot(
            kind="hist", bins=20, figsize=(8, 5), title="Order Value Distribution"
        )
        plt.xlabel("Order Amount")
        plt.tight_layout()
        plt.savefig("output/figures/order_distribution.png")
        plt.clf()

    def generate_report(self, results):
        """
        Generate a human-readable summary report.
        """
        with open("output/summary_report.txt", "w") as f:
            f.write("Sales Analytics Summary Report\n")
            f.write("-" * 40 + "\n")
            f.write(f"Total revenue: {results['total_revenue']} \n")
            f.write(f"aov: {results['aov']}\n")
            f.write(f"Unique Customers: {results['customer_count']}\n\n")
            f.write("Top customers:\n")
            f.write(results["top_customers"].to_string())