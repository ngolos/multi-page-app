import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Pets Supplements", page_icon="🐾", layout="wide")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

url_csv = "https://raw.githubusercontent.com/ngolos/ns-streamlit/main/july_pets4.csv"

@st.cache
def get_data():
    #df = pd.read_csv(url_csv, keep_default_na=False)
    df=pd.read_csv(url_csv, parse_dates=['Date First Available'], keep_default_na=False)
    df[["Price", "Mo. Revenue","D. Sales"]] = df[["Price", "Mo. Revenue","D. Sales"]].apply(pd.to_numeric)
    #df['Mo_Revenue_Mln']=(df['Mo. Revenue']/1000000).round(4)
    #df['Mo. Revenue'] = df['Mo. Revenue'].astype(str).astype(float, errors='ignore')
    #df['Sales_Mln'] = (df['Sales_Mln']).round(2)
    return df


st.title('Pets Report')
"""
Category overview .
"""
df = get_data()


# Filters
#st.sidebar.header('User Input Features')
#product_choice = []

#product_type = df['Sup_Type'].drop_duplicates()
#product_choice = st.sidebar.multiselect('Select product form:', options=sorted(product_type), default='Capsules')

#category list
#function_type=['Beauty', 'Body', 'Brain', 'Digest', 'Energy', 'Fitness', 'Immune', 'Joints', 'Multi', 'Stress_Sleep','Weight_Mngm' ]
#function_choice = st.sidebar.selectbox('Select functionality:', function_type)

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
#with st.echo():
col1, col2, col3 = st.columns(3)
with col1:
    #col1.metric(label="Dogs", value="%.2f" % total_sales_dogs)
    col1.metric(label="🐶Dogs", value=(f"$ {total_sales_dogs:,} Mln"))
with col2:
    col2.metric(label="🐶🐱Cats&Dogs", value=(f"$ {total_sales_catsdogs:,} Mln"))
with col3:
    col3.metric(label="🐱Cats", value=(f"$ {total_sales_cats:,} Mln"))
st.write("---")

a=df.groupby(['Sub-Category'])[['Mo_Revenue_Mln']].sum().sort_values('Mo_Revenue_Mln', ascending=False).reset_index()
sub_category_list = a['Sub-Category'].tolist()



st.header('Explore Sales by Target, Brand and Product')
target_type = df['Type'].drop_duplicates()
target_choice = st.multiselect('Select your target from 3 options:', options=sorted(target_type), default='Dogs')

#Filter df based on selection
filterd_type_df = df[df['Type'].isin(target_choice)]
#filterd_type_df
by_group=filterd_type_df.groupby(['Type', 'Sub-Category'])[['Mo_Revenue_Mln']].sum().sort_values(['Type','Mo_Revenue_Mln'], ascending=[False,False]).round(2).reset_index()
cat2=filterd_type_df.groupby(['Type', 'Brand']).agg(Sales_Mln=('Mo_Revenue_Mln', 'sum')).sort_values(by="Sales_Mln", ascending=False).head(15).reset_index()
cat3=filterd_type_df.groupby(['Type', "Brand", 'Product Name']).agg(Sales_Mln=('Mo_Revenue_Mln', 'sum')).sort_values(by="Sales_Mln", ascending=False).head(50).reset_index()
#by_group
chart=alt.Chart(by_group).mark_bar().encode(
    x=alt.X('Mo_Revenue_Mln:Q'),
    y=alt.Y("Sub-Category:N", sort=['Fish Oil Supplements','Probiotics','Multivitamins','Herbal Supplements','Antioxidants','Misc','Amino Acids']),
    #column='Sub-Category',
    color=('Type:N'),
    tooltip=('Type','Mo_Revenue_Mln'),
    #facet=alt.Facet('Sub-Category:N', columns=4, sort=sub_category_list),
).properties(height=300)

chart2=alt.Chart(cat2).mark_bar().encode(
    x=alt.X('Sales_Mln:Q'),
    y=alt.Y("Brand:N",sort='-x'),
    #column='Sub-Category',
    color=('Type:N'),
    tooltip=('Type','Sales_Mln'),
    #facet=alt.Facet('Sub-Category:N', columns=4, sort=sub_category_list),
).properties(height=300)



col1, col2, col3 = st.columns((1,1,2))
with col1:
    #col1.metric(label="Dogs", value="%.2f" % total_sales_dogs)
    st.subheader("Sales Split by Functionality:")
    st.altair_chart(chart)
with col2:
    st.subheader("Top Brands:")
    st.altair_chart(chart2)
with col3:
    st.subheader("Top Products:")
    st.dataframe(cat3.head(10))
