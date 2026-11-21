import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd
import pickle
import streamlit as st

# load the model
model = load_model('model.h5')

#load the pcikle files

with open('encoder_geo.pkl','rb') as file:
    label_encoded_geo = pickle.load(file)
with open('label_encoder_gender.pkl','rb') as file:
    label_encoded_gender = pickle.load(file)
with open('Scalar.pkl','rb') as file:
    label_encoded_scalar = pickle.load(file)    

# write the streamlite body
st.title('Churn Prediction Model')

# User input
geography = st.selectbox('Geography', label_encoded_geo.categories_[0])
gender = st.selectbox('Gender', label_encoded_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])


input_data = pd.DataFrame(
    {
    'CreditScore': [credit_score],
    'Gender': [label_encoded_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
}
)
# Creating a Geograhy df
input_df_geo = label_encoded_geo.transform([[geography]]).toarray()
input_df_geo_df = pd.DataFrame(input_df_geo,columns=label_encoded_geo.get_feature_names_out(['Geography']))

#concat both data
input_og = pd.concat([input_data.reset_index(drop=True),input_df_geo_df],axis=1)

#scaled the data
Scaled_data = label_encoded_scalar.transform(input_og)

#prediction of model
prediction = model.predict(Scaled_data)
prediction_prob = prediction[0][0]

st.write(f'Prediction probablitiy is : {prediction_prob:.2f}')

if prediction_prob > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')
