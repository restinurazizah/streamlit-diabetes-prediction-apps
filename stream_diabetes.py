import pickle 
import streamlit as st 

#membaca model 
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title('Data Mining for Diabetes Prediction')

#membagi kolom
col1, col2 = st.columns(2)

with col1 : 
    Pregnancies = st.text_input ('Input Pregnancies Value')

with col2 :
    Glucose = st.text_input ('Input Glucose Value')

with col1 :
    BloodPressure = st.text_input ('Input BloodPressure Value')

with col2 :
    SkinThickness = st.text_input ('Input SkinThickness Value')

with col1 :
    Insulin = st.text_input ('Input Insulin Value')

with col2 :
    BMI = st.text_input ('Input BMI Value')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('Input DiabetesPedigreeFunction Value')

with col2 :
    Age = st.text_input ('Input Age  Value')

#code prediction 

diab_diagnosis = ' '

#membuat tombol prediksi 
if st.button('Test Diabetes Prediction') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_diagnosis[0] == 1):
        diab_diagnosis = 'Patient NOT AFFLICTED with diabetes'
    else :
        diab_diagnosis = 'Patient AFFLICTED with diabetes'
    st.success(diab_diagnosis)

