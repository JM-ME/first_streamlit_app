import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Hi this is Jitendra Diner club')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Oatmeal')
streamlit.text(' 🥗 Milk')
streamlit.text(' 🐔 Egg Ommlatte')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=my_fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick some Fruit",my_fruit_list.index,['Apple','Avocado'])
fruit_list_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruit_list_to_show)



