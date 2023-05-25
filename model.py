import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score
import pickle

#load the dataset
df = pd.read_csv('LoanApprovalPrediction.csv')

#drop Load_ID column
df.drop(['Loan_ID'], axis = 1, inplace = True)

#convert categorical to int objects
label_encoder = LabelEncoder()
obj = (df.dtypes == 'object')
#print(list(obj[obj].index))#list of categorical objects
for col in list(obj[obj].index):
    df[col] = label_encoder.fit_transform(df[col])

#fill in the missing rows
for i in df.columns:
    df[i] = df[i].fillna(df[i].mean())

#divide the model into features and target variable
X= df.drop(['Loan_Status'],axis=1)
y = df['Loan_Status']

#split into training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =  train_test_split(X, y ,test_size=0.3, random_state=7)

#define the model
model = RidgeClassifier()

#fit the model on the training data
model.fit(X_train,y_train)

#save the train model
with open('train_model.pkl',mode ='wb') as pkl:
    pickle.dump(model,pkl)