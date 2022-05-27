
import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title('Real Time order prediction')

from PIL import Image
image = Image.open('train.png')







st.image(image, caption='crmb')


st.write('This app predicts the order time  based on the location amd the status based on the historical data')

st.write('This app predicts the order time  based on the orders information in real time')





# Title of the app page
st.title('Order time prediction App')

# Add a heading for input features
st.subheader('Enter  Features for Predictions')

 # Rwquest for input fatures, but replod with some default values
order_id= st.number_input('order_id', 1.0)

st.write(' Your order_id', order_id)

location_id= st.number_input('location_id', 1.0)

st.write('Your location_id is', location_id)

total= st.number_input('total', 1.0)

st.write('Your total is', total)

order_status_class= st.selectbox('order_status_class', ['READY=5', 'PREPARING=4', 'PAYMENT_PENDING=4', 'PENDING=2', 'OPEN=1'])


status_class= st.number_input('status_class', 1.0)


st.write('Your status_class is', status_class)


st.write('The model made a prediction for each customer`')

customer_id= st.number_input('customer_id', 1.0)

st.write('Your customer_id is', customer_id)

# Load  the model from disk


if st.button("Predict"):
    pickle_in = open('model.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict([[order_id,location_id,total,status_class,customer_id]])
  

    st.text(f"""
     The predicted order_time in seconds is :  {predict[0]} 
    """)    # Get the input features
    # run predictions

from PIL import Image
image = Image.open('timeline.png')



