
import streamlit

import requests


from urllib.error import URLError
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Spinach,🐔 🥑 Eggs')
streamlit.text('Espresso,🍞 Bread')
streamlit.text('🥗Blueberry Oat meal & Mango smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas  
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 


fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
#streamlit.text(fruityvice_response.json()) # writes data to the screen
# takes the json and normalizes
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as E:
  streamlit.error()
    






import snowflake.connector

streamlit.header("The fruit load list contains:")
def get_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_list()
  streamlit.dataframe(my_data_rows)
streamlit.stop()
def ins_row(new):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding" + new
add = streamlit.text_input('What fruit would you like to add?')
if streamlit.button("Add a fruit to the list"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=ins_row(add)
  streamlit.text(back_from_function)





