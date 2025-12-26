import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Zaniah | Stocks & US Economy Dashboard",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Add custom CSS for nav spacing
st.markdown(
    """
    <style>
        
        .stAppToolbar {
            padding-left: 5rem;
            padding-right: 5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

pages = [
    st.Page("home.py", title="Home", icon=":material/home:"),
    st.Page("stock_analysis.py", title="Stock Analysis", icon=":material/finance_mode:"),
    st.Page(
        "economic_indicators.py",
        title="economic_indicators",
        icon=":material/currency_exchange:",
    ),
    st.Page("correlations.py", title="Correlations", icon=":material/scatter_plot:"),
    st.Page("about.py", title="About", icon=":material/info:"),
]

page = st.navigation(pages, position="top")
page.run()


