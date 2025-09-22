# 🏡 Predicting Boston Housing Prices

This project is part of the **Machine Learning Engineer Nanodegree** under the section **Model Evaluation & Validation**.  
The goal is to build a model capable of predicting housing prices in Boston using selected features.

---

## 📌 Project Overview
- **Dataset:** Boston Housing Dataset (`housing.csv`).
- **Objective:** Predict the median value of owner-occupied homes (`MEDV`) using features:
  - `RM`: Average number of rooms per dwelling.  
  - `LSTAT`: Percentage of lower income population.  
  - `PTRATIO`: Student-to-teacher ratio.  

---

## 📂 Steps in the Project

### 1. Data Exploration
- Loaded the dataset and displayed the first 5 rows.  
- Collected dataset information:  
  - Shape: **489 data points × 4 variables**.  
  - Target variable: `MEDV`.  
- Calculated statistics:
  - Minimum price: **$105,000**  
  - Maximum price: **$1,024,800**  
  - Mean price: **$454,342.94**  
  - Median price: **$438,900**  
  - Standard Deviation: **$165,171.13**

### 2. Feature Observations
- **RM:** Positively correlated with `MEDV`. More rooms → higher price.  
- **LSTAT:** Negatively correlated with `MEDV`. Higher % of lower income → lower price.  
- **PTRATIO:** Negatively correlated with `MEDV`. Higher student-to-teacher ratio → lower price.  

### 3. Model Evaluation
- Implemented **R² Score** as the evaluation metric.
- Example result: `R² = 0.923` → Model explains **92.3%** of the variance.  
- Dataset split: **80% training, 20% testing** (to avoid overfitting/underfitting).

### 4. Learning Curves
- Trained **Decision Tree Regressor** with different `max_depth` values (1, 3, 6, 10).  
- Visualized learning curves to analyze performance on training and testing sets.

---

## 📊 Visualizations
Scatter plots show relationships between features and target (`MEDV`):

- **RM vs MEDV** → Positive correlation.  
- **LSTAT vs MEDV** → Negative correlation.  
- **PTRATIO vs MEDV** → Negative correlation.  

Learning curves for decision trees demonstrate the trade-off between model complexity and generalization.

---

## 🛠️ Technologies Used
- **Python 3**  
- **NumPy, Pandas** → Data manipulation  
- **Matplotlib, Seaborn** → Visualization  
- **scikit-learn** → Model building, R² Score, Decision Tree Regressor  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/boston-housing-prediction.git
