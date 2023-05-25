# Loan Eligibility Prediction
This project focuses on predicting loan eligibility for applicants using machine learning techniques. The project utilizes the Ridge Classifier algorithm to build a predictive model that determines whether an applicant is eligible for a loan or not.

## Dataset
The dataset used for this project is sourced from Kaggle and contains various attributes such as age, income, employment status, credit history, and loan amount. The dataset has been preprocessed to handle missing values, outliers, and feature scaling to ensure optimal model performance.

## Methodology
**Data Collection:** The dataset is collected from Kaggle, a reputable platform for datasets and machine learning competitions.

**Data Preprocessing:** The dataset undergoes preprocessing steps such as handling missing values, encoding categorical variables, and feature scaling to prepare it for model training.

**Feature Selection:** Relevant features are selected based on their importance in predicting loan eligibility. This helps in reducing dimensionality and improving model performance.

**Model Training:** The Ridge Classifier algorithm is chosen for its ability to handle binary classification tasks. The model is trained using the labeled dataset, with loan eligibility considered the target variable.

**Model Evaluation:** The trained model is evaluated using various performance metrics such as accuracy, precision, recall, and F1-score. The Ridge Classifier achieves an accuracy of 82%, indicating its effectiveness in predicting loan eligibility.

**Deployment:** The loan eligibility prediction system is deployed using Streamlit, a Python library for creating interactive web applications. The deployed system allows users to input their information and receive an instant prediction on their loan eligibility. 

**Results**
The Ridge Classifier model achieves an accuracy of 82% in predicting loan eligibility. This performance demonstrates the effectiveness of the model in making accurate predictions based on the given features.

## Project Repository 
The project repository can be found on GitHub at https://github.com/santhulak/Loan-Eligibility-Prediction. It contains the following files:

LoanApprovalPrediction.csv: This dataset used for training and testing the model.
Loan Eligibility Prediction.ipynb: Jupyter Notebook containing the data preprocessing, model training and evaluation process.
app.py: Streamlit application code for deploying the model.
requirements.txt: File listing the required Python packages for running the application.
README.md: Detailed information about the project, including instructions for running the application.

**Usage**
To access the loan eligibility prediction system, follow these steps:

Access the deployed application on the Streamlit Cloud platform using the provided URL

Input the necessary information, such as age, income, employment status, credit history, and loan amount.

Click on the "Predict" button to obtain the loan eligibility prediction.

Conclusion
The Loan Eligibility Prediction project successfully utilizes the Ridge Classifier algorithm to predict loan eligibility for applicants. The project involves data collection from Kaggle, preprocessing of the dataset, model training, evaluation, and deployment using Streamlit Cloud.
