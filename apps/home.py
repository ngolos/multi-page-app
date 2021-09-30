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
