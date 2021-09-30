import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def app():
    url_csv = "https://raw.githubusercontent.com/ngolos/ns-streamlit/main/july_pets4.csv"

    @st.cache
    def get_data():
        #df = pd.read_csv(url_csv, keep_default_na=False)
        df=pd.read_csv(url_csv, parse_dates=['Date First Available'], keep_default_na=False)
        df[["Price", "Mo. Revenue","D. Sales"]] = df[["Price", "Mo. Revenue","D. Sales"]].apply(pd.to_numeric)
        return df


    st.title('Pets Report')
    """
    Category overview .
    """
    df = get_data()

    st.write(df)
    st.header('Page 1 - Explore the Largest Ingredient Groups for each Product Form')
    #st.dataframe(df)

    # TOP KPI's
    total_sales_all = df["Mo_Revenue_Mln"].sum().round(2)
    total_sales_dogs = df.query('Type=="Dogs"')["Mo_Revenue_Mln"].sum().round(2)
    total_sales_cats = df.query('Type=="Cats"')["Mo_Revenue_Mln"].sum().round(2)
    total_sales_catsdogs = df.query('Type=="Cats&Dogs"')["Mo_Revenue_Mln"].sum().round(2)
    #average_rating = round(df_selection["Rating"].mean(), 1)
    #star_rating = ":star:" * int(round(average_rating, 0))
    #average_sale_by_transaction = round(df_selection["Total"].mean(), 2)
    st.write("---")
    st.header(f'Total Sales (30 days) Amz Best Sellers:$ {total_sales_all:,} Mln')
    #  with st.echo():
    col1, col2, col3 = st.columns(3)
    with col1:
        #col1.metric(label="Dogs", value="%.2f" % total_sales_dogs)
        col1.metric(label="🐶Dogs", value=(f"$ {total_sales_dogs:,} Mln"))
    with col2:
        col2.metric(label="🐶🐱Cats&Dogs", value=(f"$ {total_sales_catsdogs:,} Mln"))
    with col3:
        col3.metric(label="🐱Cats", value=(f"$ {total_sales_cats:,} Mln"))
    st.write("---")
