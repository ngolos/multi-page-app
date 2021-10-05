import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here
from streamlit_lottie import st_lottie
import requests

app = MultiApp()
st.set_page_config(page_title="Pets Supplements", page_icon="🐾", layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0.5

st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

file_url = 'https://assets2.lottiefiles.com/packages/lf20_v7nRH3.json'
lottie_dog = load_lottieurl(file_url)
st_lottie(lottie_dog, speed=1, height=150, key="initial")

st.markdown("<h1 style='text-align: center; color: red;'>Pets Report</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: black;'>This interactive report is created as an example of explatory sales data analysis report for Amazon's Categories.</p>", unsafe_allow_html=True)



# Add all your application here
app.add_app("Overview", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
# The main app
app.run()
