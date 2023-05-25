import streamlit as st
import pickle

def main():
    bg = """<div style ='backgroung-color:blue; padding:15px'>
            <h1 style='color:white'> Loan Eligibility Prediction Streamlit App</h1>
            </div>"""
    st.markdown("<h1 style='text-align: center; color:Blue;'>Loan Eligibility Prediction </h1>",
                 unsafe_allow_html=True)
    #st.markdown(bg, unsafe_allow_html=True)

    left, right = st.columns((2,2))
    gender = left.selectbox('Gender', ('Male','Female'))
    married = right.selectbox('Married', ('Yes', 'No'))
    dependent = left.selectbox('Dependents', ('None','One','Two','Three') )
    education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
    self_employed = left.selectbox('Self-Employed', ('Yes', 'No'))
    applicant_income = right.number_input('Applicant Income')
    coApplicantIncome = left.number_input('Coapplicant Income')
    loanAmount = right.number_input('Loan Amount')
    loan_amount_term = left.number_input('Loan Tenor (in months)')
    creditHistory = right.number_input('Credit History', 0.0, 1.0)
    propertyArea = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))
    button = st.button('Predict')

    #if button is clicked make prediction
    if button:
        result = predict(gender, married, dependent, education, self_employed, applicant_income,
                        coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea)
        st.success(f"You are {result} for the loan.")

#Load the train model
with open('train_model.pkl','rb') as pkl:
    train_model = pickle.load(pkl)

def predict(gender, married, dependent, education, self_employed, applicant_income,
                        coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea):
        
        #processing user input
        gen = 0 if gender == 'Male' else 1
        mar = 0 if married == 'Yes' else 1
        dep = float(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
        edu = 0 if education == 'Graduate' else 1
        sem = 0 if self_employed == 'Yes' else 1
        pro = 0 if propertyArea == 'Semiurban' else 1
        loAm = loanAmount / 1000
        cap = coApplicantIncome / 1000
        #making predictions
        prediction = train_model.predict([[gen,mar,dep,edu,sem,applicant_income,cap,loAm,loan_amount_term,creditHistory,pro]])
        verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
        return verdict

if __name__ == '__main__':
     main()

