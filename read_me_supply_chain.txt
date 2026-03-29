# Business Analytics Project: Supply Chain Delivery Delay Prediction

## Project Overview
This project was developed as part of a Business Analytics course.  
The objective is to predict whether a delivery will be delayed using machine learning techniques and to analyze the key factors influencing delivery performance.

---

## Dataset
The dataset includes information related to:
- Orders
- Customers
- Products
- Shipping operations

Key features include:
- Shipping Mode
- Order Region
- Sales and Profit
- Delivery Status

---

## Data Preprocessing
- Cleaned missing and inconsistent data  
- Converted categorical variables into numerical format  
- Split the data into training and testing sets  

---

## Model
- Model used: Random Forest Classifier  
- Accuracy: approximately 81%  

The model demonstrates good performance in predicting both delayed and on-time deliveries.

---

## Model Explainability (SHAP)
SHAP was used to interpret the model’s predictions.

- Identifies the impact of each feature on delay risk  
- Highlights the most influential variables affecting predictions  

---

## Dashboard (Power BI)
A Power BI dashboard was developed to visualize key insights:

- Delivery delay percentage  
- Sales performance by region  
- Impact of shipping mode on delays  
- Interactive filtering capabilities  

---

## Bias and Fairness Analysis
- Bias was analyzed using the Shipping Mode feature  
- Some variation across groups was observed, but no strong evidence of significant bias was found  

---

## Key Insights
- Shipping methods influence delivery delays  
- Certain regions experience higher delay rates  
- Order characteristics affect delivery performance  

---

## Tools Used
- Python  
- Pandas and NumPy  
- Scikit-learn  
- SHAP  
- Power BI  

---

## Additional Implementation
- A pipeline was implemented using ColumnTransformer and Pipeline  
- The trained model was saved using joblib  
- A scoring script was created to generate predictions on new data  

---

## Conclusion
Machine learning can effectively predict delivery delays and provide valuable insights to support logistics optimization and decision-making.

Note: The trained model file is not included due to GitHub file size limitations.
---

## Author
Taqwa Almohammedi  
Business Analytics Student