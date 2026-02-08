from analyzer import SalesAnalyser

"""
main.py

Entry point of the Sales Analytics Platform.

This file is responsible ONLY for orchestration:
- initializing the analyzer
- triggering data loading and cleaning
- running analytics
- generating reports and visualizations

Business logic and data processing are intentionally
kept outside of this file to ensure clean architecture.
"""

def main():
    """
    Main execution workflow of the project.
    This function defines the order of operations
    without containing any business logic.
    """

    analyzer = SalesAnalyser()

    # Load raw sales data from CSV 
    analyzer.load_data()
    
    # Clean and validate the dataset, then export cleaned CSV
    analyzer.clean_data()

    # Run analytical computations and business metrics
    results = analyzer.analytics()

    # Generate visualizations and save them as PNG files
    analyzer.create_visualizations()

    # Generete summary report
    analyzer.generate_report(results)
    


if __name__ == "__main__":
    # Ensures the script runs only when ezecuted directly
    main()