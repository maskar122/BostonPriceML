import streamlit as st
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Train the model when the app runs
def train_model():
    # Sample training data (replace with actual data)
    X_train = np.array([[5, 34, 15], [4, 55, 22], [8, 7, 12]])
    y_train = np.array([400000, 150000, 1000000])

    # Create and train a Decision Tree model
    reg = DecisionTreeRegressor(max_depth=5)
    reg.fit(X_train, y_train)
    
    return reg

# Train the model directly
reg = train_model()

# Streamlit UI
st.title("Boston House Price Prediction")

# User inputs
rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, step=1)
poverty = st.number_input("Neighborhood Poverty Level (%)", min_value=0, max_value=100, step=1)
student_teacher_ratio = st.number_input("Student-Teacher Ratio", min_value=1, max_value=50, step=1)

# Prediction button
if st.button("Predict Price"):
    input_data = np.array([[rooms, poverty, student_teacher_ratio]])
    predicted_price = reg.predict(input_data)[0]
    st.success(f" Predicted Price: ${predicted_price:,.2f}")
