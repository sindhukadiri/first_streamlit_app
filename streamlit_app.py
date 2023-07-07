
import streamlit


import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Spinach,🐔 🥑 Eggs')
streamlit.text('Espresso,🍞 Bread')
streamlit.text('🥗Blueberry Oat meal & Mango smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas  
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 


fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json()) # writes data to the screen
# takes the json and normalizes
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output on screen
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


#othr txt box
fruit_choice2 = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', fruit_choice2)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")



