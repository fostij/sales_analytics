# Sales Analytics Platform

## Project Overview
This project is a Sales Analytics Platform developed as part of a Python Programming
and Data Analysis course. The goal is to apply object-oriented design, data analysis,
algorithmic thinking, and visualization techniques in a real-world-style project.

---

## Features
- Object-oriented data models with validation
- Data loading, cleaning, and preprocessing using Pandas
- Business analytics and key performance metrics
- Custom sorting and searching algorithms with complexity analysis
- Data visualization using Matplotlib
- Clean project structure and version control with Git

---

## Project Structure

sales-analytics/
|--- data/
|    |--- sales_data.csv
|    |___ sales_clean.csv
|--- output/
|     |--- sumary_report.txt
|     |___ figures/
|       |--- monthly_trend.png
        |--- order_distribution.png
        |___ revenue_by_category.png
|--- algorithms.py
|--- analyzer.py
|--- main.py
|--- models.py
|--- utils.py
|--- requirements.txt
|--- README.md


# Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/fostij/sales_analytics.git
cd sales-analytics

2. Install dependencies:
pip install -r requirements.txt

3. Run the project:
python main.py


## Analytics Performed
- Total revenue
- Average order value
- Customer count
- Revenue by product category
- Top 10 customers by revenue
- Order status distribution
- Mothly revenue trends
- Order value distribution

## Algorithm Performance Comparison:

Custom Bubble Sort:
- Time Complexity: O(n^2)
- Execution time significantly slower for large datasets

Built-in sorted():
- Time Complexity: O(n log n)
- Implemented in optimized C code (Timsort)

Conclusion:
Built-in sorting functions are more efficient and should be used in production,
while custom algorithms are useful for learning and analysis.

## Technologies Used
- Python
- Pandas
- Numpy 
- Matplotlib
- Git & GitHub

## Author 
Oleg
