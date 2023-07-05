import streamlit
import pandas
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Spinach,🐔 🥑 Eggs')
streamlit.text('Espresso,🍞 Bread')
streamlit.text('🥗Blueberry Oat meal & Mango smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
