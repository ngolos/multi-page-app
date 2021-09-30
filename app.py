import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

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

st.title('Pets Report')
"""
This is supposed to be a multipage framework.
- Page 1: Product form - Ingredient based view.
- Page 2: function based view.
- Page 3: could be google trends, etc. All the data is based on June'2020 Amazon BSL in Dietaty Supplements Category.
- Currently I use a singe page mode.
"""



# Add all your application here
app.add_app("Overview", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
# The main app
app.run()
