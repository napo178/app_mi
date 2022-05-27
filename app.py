
import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title('Real Time order prediction')
from PIL import Image
image = Image.open('crmb.png')
st.image(image, caption='crmb')





st.title('The app uses the real time inputs to predict the final order time')



from PIL import Image
image = Image.open('timeline.png')
st.image(image, caption='Problem')



# Add a heading for input features
st.subheader('Enter  Features for Predictions')

 # Rwquest for input fatures, but replod with some default values
Order_id= st.number_input('order_id', 1.0)

st.write(' The order_id:', Order_id)

Location_id= st.number_input('location_id', 1.0)

st.write('The location_id is:', Location_id)

Total= st.number_input('total', 1.0)

st.write('The total is:', Total)

order_status_class= st.selectbox('order_status_class', ['READY=5', 'PREPARING=4', 'PAYMENT_PENDING=4', 'PENDING=2', 'OPEN=1'])


Status_class= st.number_input('status_class', 1.0)


st.write('The status_class is', Status_class)




st.write('(The model made a prediction for each customer)')



Customer_id= st.number_input('customer_id', 1.0)

st.write('Your customer_id is', Customer_id)

# Load  the model from disk


if st.button("Predict"):
    pickle_in = open('model.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict([[Order_id,Location_id,Total,Status_class,Customer_id]])
  

    st.text(f"""
     The predicted order_time in seconds is :  {predict[0]} 
    """)    # Get the input features
    # run predictions

from PIL import Image
image = Image.open('timeline.png')



