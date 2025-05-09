# Boston House Price Prediction  

This repository contains a project focused on predicting housing prices in Boston using a regression model. The dataset includes features such as crime rate, number of rooms, and proximity to facilities. By preprocessing data, exploring relationships, and building a model, this project aims to provide accurate predictions and insights into factors influencing Boston housing prices.  

---

## **Features**  

- **Data Preprocessing**:  
  - Handle missing values using imputation methods.  
  - Standardize data to improve model performance.  

- **Exploratory Data Analysis**:  
  - Correlation heatmaps and feature visualizations to uncover trends.  

- **Modeling**:  
  - Linear Regression is used to predict housing prices.  
  - Performance is evaluated with metrics such as Mean Squared Error (MSE) and R² Score.  

- **Visualization**:  
  - Scatter plots to compare actual vs. predicted prices.  
  - Heatmaps for feature correlation analysis.  

---

## **Dataset**  

The dataset contains 13 predictor variables and 1 target variable (`MEDV` - Median value of homes).  

| **Feature** | **Description** |  
|-------------|-----------------|  
| CRIM        | Crime rate per capita |  
| ZN          | Proportion of residential land zoned for large lots |  
| RM          | Average number of rooms per dwelling |  
| DIS         | Weighted distances to employment centers |  
| TAX         | Full-value property tax rate |  
| MEDV        | Median value of owner-occupied homes (Target Variable) |  

---


## **Outputs**  
- Correlation heatmap for feature relationships.  
- Model evaluation metrics (MSE, RMSE, and R² Score).  
- Scatter plot showing actual vs. predicted prices.  

## **Results**  
The model's performance is summarized as follows:  
- **Mean Squared Error (MSE):** calculated value  
- **Root Mean Squared Error (RMSE):** calculated value  
- **R² Score:** calculated value  

## **Key Visualizations**  

### **Correlation Heatmap**  
Displays relationships between features and the target (MEDV).  

### **Actual vs. Predicted Prices**  
Visual comparison of the predicted prices vs. the actual values.  

## **Technologies Used**  
- Python 3.8+  
- Libraries:  
  - pandas  
  - numpy  
  - matplotlib  
  - seaborn  
  - scikit-learn  

