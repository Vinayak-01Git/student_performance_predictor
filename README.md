🎓 Student Performance Predictor (End-to-End MLDLC)

An end-to-end Machine Learning web application that predicts a student's final academic score based on their daily habits, study patterns, and academic history. Built using a complete **Machine Learning Development Life Cycle (MLDLC)** approach, transitioning from exploratory data analysis to a local and cloud-deployed production model.

### 🚀 Live Demo
Experience the live, interactive web application here: https://studentperformancepredictor12.streamlit.app/

## 🛠️ Tech Stack Used
* **Data Science & Analytics:** Python, Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Linear Regression, Label Encoding, Data Validation)
* **Model Serialization:** Pickle (Pipeline Exporting)
* **Web Deployment:** Streamlit Community Cloud (Responsive UI Design)

---

## 📋 Features & Architecture

The application accepts 5 key student metrics to compute predictions instantly:
1. **Hours Studied** (Numeric Input)
2. **Previous Scores** (Academic Baseline)
3. **Extracurricular Activities** 
4. **Sleep Hours** (Rest Metrics)
5. **Sample Question Papers Practiced** (Interactive Slider)


## 📁 Repository Structure

```text
├── model.ipynb          # Jupyter Notebook: Data Cleaning, EDA, Model Training & Export
├── student_model.pkl    # Serialized Weights of the Trained Linear Regression Model
├── app.py               # Streamlit Production Frontend Script
├── requirements.txt     # Locked Dependency Configurations for Cloud Deployment
└── README.md            # Professional Project Documentation
