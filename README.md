Business Analytics Project: Supply Chain Delivery Delay Prediction
Project Overview

This project was developed as part of a Business Analytics course.
The objective is to predict whether a delivery will be delayed using machine learning and to provide actionable insights for improving logistics performance.

Dataset

The dataset includes information about:

Orders
Customers
Products
Shipping operations

Key features include:

Shipping Mode: e.g., First Class, Same Day
Order Region: Customer location
Product Category
Benefit per Order: Profit per order
Delivery Status: On-time or delayed

The dataset contains 180,519 observations and 53 features, enabling a detailed analysis of delivery performance and delay risks.

Data Preprocessing
Cleaned missing and inconsistent data
Converted categorical variables into numerical format
Scaled features for models requiring standardization (e.g., Logistic Regression)
Split the data into training and testing sets
Machine Learning Model
Model used: Random Forest Classifier
Model Selection: Compared Logistic Regression, Decision Tree, and Random Forest using a sampled training subset for faster experimentation
Hyperparameter Tuning: Performed using RandomizedSearchCV
Performance:
Accuracy: 0.81
Precision (Delayed orders): 0.88
Recall (Delayed orders): 0.75
F1-Score: 0.81
5-Fold Cross-Validation Average: 0.77
Confusion Matrix Insight: Correctly identified ~14,800 delayed orders; ~5,000 delayed orders were missed
Impact: Enables early detection of high-risk shipments to support proactive decisions

The model was saved using joblib and a scoring script (scoring.py) was implemented to generate predictions on new data.

Model Explainability (SHAP)

SHAP (SHapley Additive Explanations) was used to interpret the model’s predictions:

Highlights which features increase or decrease delivery delay risk
Identifies key drivers: Type of product, Benefit per order, Shipping Mode
Provides actionable insights for logistics optimization
Dashboard (Power BI)

A Power BI dashboard was developed to visualize insights:

Delivery delay percentage by region and shipping mode
Sales performance trends
Identification of high-risk orders
Interactive filtering for real-time analysis
Bias and Fairness Analysis
Shipping Mode was analyzed for potential bias
Minor variations were observed, but no evidence of significant unfairness was found
Key Insights
Shipping methods strongly influence delays
Certain regions consistently experience higher late deliveries
Order characteristics, like product type and profit, affect risk patterns
Peak months with high sales require additional logistics capacity
Tools Used
Python (Pandas, NumPy, Scikit-learn)
SHAP for model interpretability
Power BI for interactive dashboards
Joblib for model persistence
Implementation Highlights
Data preprocessing and feature engineering handled via Pipeline and ColumnTransformer
Random Forest model trained, tuned, and validated
Predictions for new orders handled with scoring.py pipeline
Conclusion

Machine learning effectively predicts delivery delays and highlights actionable insights to improve logistics, reduce operational costs, and increase customer satisfaction.

Author

Taqwa Almohammedi
Business Analytics Student
