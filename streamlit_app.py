# Import python packages
import streamlit as st

##connection info
##st.secrets["SNOWFLAKE_ACCOUNT"] = "ZRB74007"
##st.secrets["SNOWFLAKE_USERNAME"] = "MASAKIMACHIOKA"
##st.secrets["SNOWFLAKE_HOST"] = "INZRLSU-ZRB74007.snowflakecomputing.com"
##st.secrets["SNOWFLAKE_PASSWORD"] = ""
account = st.secrets["SNOWFLAKE_ACCOUNT"]
username = st.secrets["SNOWFLAKE_USERNAME"]
host = st.secrets["SNOWFLAKE_HOST"]
password = st.secrets["SNOWFLAKE_PASSWORD"]
# Snowflake接続
##cnx = st.snowflake.connect(
##    user=username,
##    password=password,
##    account=account,
##    host=host,
##)
# Snowflake接続
cnx = st.connection(
    "snowflake",
    username=username,
    password=password,
    account=account,
    host=host,
)





##from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(  f":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
##st.write(
##  _ = """Replace this example with your own code!
##  **And if you're new to Streamlit,** check
##  out our easy-to-follow guides at
##  [docs.streamlit.io](https://docs.streamlit.io).
##  """
##)
st.write(
    """Choose the fruits you want in your custome Smoothie!
    """
)

##_ = """
##option = st.selectbox(
##    "What is your favorite fruit?",
##    ("Banana", "Strawberries", "Peaches"),
##)

##st.write("Your favorite fruit is:", option)
##"""



name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be:", name_on_order)



## Changes Needed When Moving from SiS to SniS
##session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.sesseion()


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
##st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:"
    , my_dataframe
    , max_selections=5
)


if ingredients_list:
    ##st.write(ingredients_list)
    ##st.text(ingredients_list)

    ingredients_string = ''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    ##st.write(ingredients_string)
    
    ##my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
    ##my_insert_stmt = """ insert into smoothies.public.orders
    ##        values ('""" + ingredients_string + """','""" + name_on_order + """')"""
    my_insert_stmt = """ insert into smoothies.public.orders (ingredients, name_on_order)
        values ('""" + ingredients_string + """', '""" + name_on_order + """')"""



    
    ##st.write(my_insert_stmt)
    ##st.stop()
    
##_="""
    time_to_insert = st.button('Submit Order')
    
    ##if ingredients_string:
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        
        st.success('Your Smoothie is ordered!', icon="✅")
##"""



    



