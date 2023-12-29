import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Brakefast favorties')
streamlit.text('🐔Idly with Chickencurry-$110 2pcs')
streamlit.text('🥗 Veg Dosa-$70')
streamlit.text('🥣pongal-$50')
streamlit.text('🥑🍞Avacado with cheese Tost-$120')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
streamlit.dataframe(my_fruit_list)
