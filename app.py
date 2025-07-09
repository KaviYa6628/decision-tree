import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load the trained model
model = joblib.load("decision_tree_model.joblib")

# Set Streamlit page configuration
st.set_page_config(
    page_title="Breast Cancer Diagnosis - ML App",
    page_icon="🧠",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["🏠 Home", "📥 Predict", "📊 About Breast Cancer"])

# ------------------ Home Page ------------------
if section == "🏠 Home":
    st.title("🧠 Breast Cancer Diagnosis Using Decision Tree")
    st.markdown("""
    Welcome to the **Breast Cancer Diagnosis Web App**.

    This app uses a **Decision Tree Machine Learning model** to predict whether a breast tumor is **Malignant (cancerous)** or **Benign (non-cancerous)** based on input features from a breast cancer test report.

    🔍 The model was trained on the **Breast Cancer Wisconsin Diagnostic Dataset** using Scikit-learn.
    
    Use the side navigation to:
    - Learn more about breast cancer
    - Enter test data and get predictions
    """)

# ------------------ About Disease Page ------------------
elif section == "📊 About Breast Cancer":
    st.title("📊 Understanding Breast Cancer")
    st.image("https://www.cdc.gov/cancer/breast/images/breast-cancer.jpg", use_column_width=True)
    st.markdown("""
    **Breast cancer** is a disease in which cells in the breast grow out of control. It is one of the most common cancers among women worldwide.

    ### 📌 Key Points:
    - Early detection significantly improves the chances of successful treatment.
    - Diagnostic features such as **radius**, **texture**, **perimeter**, and **area** are used by doctors and ML models to predict malignancy.
    - This app uses these features to provide a **fast second opinion**.

    ⚠️ **Note:** This is a predictive aid, not a replacement for medical diagnosis.
    """)

# ------------------ Prediction Page ------------------
elif section == "📥 Predict":
    st.title("📥 Input Tumor Features to Predict Diagnosis")
    st.markdown("""
    Please enter the tumor measurement values below. You can either:
    - 🔹 Manually input the features
    - 🔹 Or upload a `.csv` file in the correct format
    """)

    input_method = st.radio("Choose input method", ["Manual Entry", "Upload CSV"])

    features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
                'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
                'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
                'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
                'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

    if input_method == "Manual Entry":
        user_input = {}
        with st.form("manual_input_form"):
            st.subheader("🔢 Enter Feature Values")
            for i in range(0, len(features), 3):
                cols = st.columns(3)
                for j in range(3):
                    if i + j < len(features):
                        feature = features[i + j]
                        user_input[feature] = cols[j].number_input(f"{feature}", value=0.0)
            submit_button = st.form_submit_button("Predict")

        if submit_button:
            input_df = pd.DataFrame([user_input])
            prediction = model.predict(input_df)[0]
            result = "🩸 Malignant" if prediction == 0 else "✅ Benign"
            st.success(f"Prediction: {result}")

    else:
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        if uploaded_file is not None:
            try:
                input_df = pd.read_csv(uploaded_file)
                if list(input_df.columns) != features:
                    st.error("❌ Column names do not match expected input features.")
                    st.info(f"Expected columns: {features}")
                else:
                    prediction = model.predict(input_df)
                    results = ["Malignant" if p == 0 else "Benign" for p in prediction]
                    st.write("## 🧾 Prediction Results:")
                    st.table(pd.DataFrame({"Sample": range(1, len(results)+1), "Prediction": results}))
            except Exception as e:
                st.error(f"⚠️ Error reading file: {e}")
