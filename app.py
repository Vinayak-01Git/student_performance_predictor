import streamlit as st
import pickle
import numpy as np

# 1. Loading the saved model
with open('student_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Predictor")

# 2. Input fields for the model
hours_studied = st.number_input("Hours Studied", min_value=1, max_value=9, value=8)
previous_scores = st.number_input("Previous Scores", min_value =40, max_value = 99,value = 70)
sleep_hours = st.number_input("Sleep Hours", min_value=4, max_value=9, value=7)
sample_paper_solved = st.slider("Number of Sample Papers Practiced", min_value=0, max_value=9, value=6)

# Creating a dropdown for extracurricural activities
extra_curr = st.selectbox("Participates in Extracurricular Activities?", ["Yes", "No"])

# 3. Predict button
if st.button("Predict Score"):
    # Converting 'Yes' to 1 and 'No' to 0 to match LabelEncoder
    extra_curr_encoded = 1 if extra_curr == "Yes" else 0
    
    # Passing the encoded variable into the array in the exact column order as present in the dataset.
    input_data = np.array([[hours_studied, previous_scores,extra_curr_encoded, sleep_hours, sample_paper_solved]])
    
    # Making prediction
    prediction = model.predict(input_data)
    predicted_score = round(prediction[0], 2)
    
    st.success(f"📝 Predicted Student Score: **{predicted_score}**")
    
    # Animation time
    if predicted_score >= 80:
        st.balloons()
        st.markdown("#### ❤️‍🔥 **Woohoo! Absolutely phenomenal! Keep shining!**")
        
    elif predicted_score >= 70:
        st.markdown("#### 😀 **Brilliant job! You are on the right track, keep it up!**")
        
    elif predicted_score >= 50:
        st.markdown("#### 😺 **Good effort! A little more focus and you'll comeback!**")
        
    else:
        st.markdown("#### 💪 **Don't lose heart! Consistency is key. Time to double down!**")
