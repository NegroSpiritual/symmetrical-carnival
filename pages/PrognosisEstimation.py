import streamlit as st
import random

st.set_page_config(page_title="Prognosis Estimation", page_icon="📈")
st.title('Liver Disease Prediction Form')
st.sidebar.header("Prognosis Classification")

n_days = st.number_input('N_Days', min_value=0, value=0)
    
status1 = st.selectbox('Status 1', ['Present', 'Absent'])
status2 = st.selectbox('Status 2', ['Present', 'Absent'])
drug = st.selectbox('Drug', ['D-penicillamine', 'None', 'Azathioprine', 'Steroids'])    
age = st.number_input('Age', min_value=0, value=0)
    
sex = st.selectbox('Sex', ['Male', 'Female'])
    
ascites = st.selectbox('Ascites', ['Yes', 'No'])
    
hepatomegaly = st.selectbox('Hepatomegaly', ['Yes', 'No'])
    
spiders = st.selectbox('Spiders', ['Yes', 'No'])
    
edema = st.selectbox('Edema', ['Yes', 'No'])
    
bilirubin = st.number_input('Bilirubin', min_value=0.0, value=0.0, format="%.2f")
cholesterol = st.number_input('Cholesterol', min_value=0.0, value=0.0, format="%.2f")
albumin = st.number_input('Albumin', min_value=0.0, value=0.0, format="%.2f")
copper = st.number_input('Copper', min_value=0.0, value=0.0, format="%.2f")
alk_phos = st.number_input('Alk_Phos', min_value=0.0, value=0.0, format="%.2f")
sgot = st.number_input('SGOT', min_value=0.0, value=0.0, format="%.2f")
tryglicerides = st.number_input('Tryglicerides', min_value=0.0, value=0.0, format="%.2f")
platelets = st.number_input('Platelets', min_value=0.0, value=0.0, format="%.2f")
prothrombin = st.number_input('Prothrombin', min_value=0.0, value=0.0, format="%.2f")
    
stage = st.selectbox('Stage', ['C', 'D'])
    
if st.button('Predict'):
    prediction = random.choice(["Patient will survive", "Patient will not survive"])
    st.write(f"Machine predicts: {prediction}")
