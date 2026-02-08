from analyzer import SalesAnalyser
import timeit
import random
from algorithms import bubble_sort

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


# -------------------------------------------------------
# Temporary algorithm performance test (educational only)
# This block is used to compare a custom sorting algorithm
# with Python's built-in sorted() function.
# It is not part of the core application logic.

# Generate sample data for sorting
sample_data = [random.randint(1, 10000) for _ in range(1000)]
# Measure executio time of custom bubble sort
bubble_time = timeit.timeit(
    lambda: bubble_sort(sample_data), number=1
)
# Measure execution time of Python built-in sort
builtin_time = timeit.timeit(
    lambda: sorted(sample_data), number=1
)

# Output comparison results
print("\nAlgorithm Performance Comparison:")
print(f"Custom Bubble Sort: {bubble_time: .4f}")
print(f"Built-in sorted(): {builtin_time: .4f}")
    


if __name__ == "__main__":
    # Ensures the script runs only when ezecuted directly
    main()