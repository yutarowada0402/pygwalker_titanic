from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import seaborn as sns
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
# Import your data
df = sns.load_dataset('titanic')

pyg_app = StreamlitRenderer(df)
 
pyg_app.explorer()
 