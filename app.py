
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
a_order= st.number_input('a_order', 1.0)

st.write(' The a_order is:', a_order)

a_value= st.number_input('a_value', 1.0)

st.write('The a_value is:', a_value)

question_id= st.number_input('total', 1.0)

st.write('The question_id is:',question_id)

order_status_class= st.selectbox('text_category', ['Mostly Disagree=1', 'Slightly Disagree=2', 'Slightly Agree=3', 'Mostly Agree=4'])


text_category= st.number_input('status_class', 1.0)

st.write('The status_class is', text_category)


id= st.number_input('id', 1.0)

st.write('the id is', id)


st.write('(The model made a prediction for each people in the survey)')





Customer_id= st.number_input('customer_id', 1.0)

st.write('Your customer_id is', Customer_id)

# Load  the model from disk


if st.button("Predict"):
    pickle_in = open('forest.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict([['a_order','a_value','question_id','text_category','id']])
  

    st.text(f"""
     The predicted intelligence multiple  is :  {predict[0]} 
    """)    # Get the input features
    # run predictions

from PIL import Image
image = Image.open('timeline.png')



