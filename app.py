
import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title('Real Time order prediction')

from PIL import Image
image = Image.open('crmb.png')
st.image(image, caption='crmb')
st.write('This app predicts the order time  based on the location amd the status based on the historical data')



def main():

    # Title of the app page
    st.title('Order time prediction App')

    # Add a heading for input features
    st.subheader('Enter  Feature For Predictions')

 # Rwquest for input fatures, but replod with some default values
order_id= st.number_input('order_id', 1.0)

location_id= st.number_input('location_id', 1.0)


total= st.number_input('total', 1.0)

st.selectbox('status', ['Pending=0', 'Completed=1', 'Cancelled=2'])

status_class= st.number_input('status_class', 1.0)


customer_id= st.number_input('customer_id', 1.0)


if st.button("Predict"):
    pickle_in = open('model.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict([[order_id,location_id,total,status_class,customer_id]])
  

    st.write(f"""
    ### The predicted order_time in seconds is :  {predict[0]} 
    """)    # Get the input features
    # run predictions







