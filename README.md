# 🧠 Breast Cancer Classification using Decision Tree

This project uses a Decision Tree Classifier to predict whether a breast tumor is **Malignant** or **Benign** based on medical features. It's built using the **Breast Cancer Wisconsin (Diagnostic) Dataset** and is ideal for learning and competition use.

---

## 📂 Dataset

- **Source**: [Kaggle - Breast Cancer Wisconsin Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
- **Total samples**: 569  
- **Classes**: Malignant (0), Benign (1)  
- **Features**: 30 numeric attributes such as `radius_mean`, `texture_mean`, etc.

---

## 💡 Project Features

- ✅ Data Preprocessing (Label encoding, feature-target split)
- ✅ Model Training using Decision Tree Classifier
- ✅ Accuracy Evaluation
- ✅ Confusion Matrix + Precision, Recall, F1-score
- ✅ Feature Importance Visualization
- ✅ Tree Structure Visualization
- ✅ Model Saving (`.joblib`)
- ✅ Predict from new CSV input (`user_input.csv`)

---

## 📦 Dependencies

Install these using pip:

```bash
pip install pandas matplotlib seaborn scikit-learn joblib
```

---

## 🚀 How to Run

1. **Download** `data.csv` from the Kaggle dataset  
2. Place `data.csv` and `user_input.csv` in the same folder as the script

### 🔧 Run the Python script:

```bash
python breast_cancer_decision_tree.py
```

It will:
- Train a Decision Tree
- Show feature importance bar chart
- Plot confusion matrix
- Visualize the decision tree
- Save the model as `decision_tree_model.joblib`
- Predict from a file called `user_input.csv`

---

## 📥 User Input Format (for Prediction)

Create a CSV file named `user_input.csv` with these 30 columns:

```text
radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,
compactness_mean,concavity_mean,concave points_mean,symmetry_mean,fractal_dimension_mean,
radius_se,texture_se,perimeter_se,area_se,smoothness_se,
compactness_se,concavity_se,concave points_se,symmetry_se,fractal_dimension_se,
radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,
compactness_worst,concavity_worst,concave points_worst,symmetry_worst,fractal_dimension_worst
```

### 📄 Example (`user_input.csv`):

```csv
17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,
25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189
```

Run the script again and it will output:

```
Sample 1: Benign
```

---

## 📊 Sample Output

```text
✅ Model Accuracy: 95.61 %

Classification Report:
              precision    recall  f1-score   support
 Malignant       0.96       0.93       0.94        72
    Benign       0.95       0.97       0.96        72
```

---

## 🧠 Visualization Samples

- 🔹 **Feature Importance Bar Chart**
- 🔹 **Confusion Matrix**
- 🔹 **Full Tree Plot** using `plot_tree()` from sklearn

---

## 📁 File Structure

```
├── data.csv                  # Dataset from Kaggle
├── user_input.csv            # Your own input for prediction
├── breast_cancer_decision_tree.py
├── decision_tree_model.joblib
├── README.md                 # <- You are here
```

---

## 🏁 Future Enhancements

- [ ] Add cross-validation
- [ ] GridSearchCV for hyperparameter tuning
- [ ] Convert to Streamlit App
- [ ] Use CNN for image-based prediction

---

## 🏷️ License

This project is licensed under the MIT License.
