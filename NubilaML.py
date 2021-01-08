import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from SLR import SLR
from RFR import RFR

st.title("Machine Learning for Everyone")

st.sidebar.write("""
# **Nubila ML**

""")
modelSelect_name = st.sidebar.selectbox(
    "Select a Regression Model", ("Simple Linear Regression", "Random Forest Regression"))


if modelSelect_name == "Simple Linear Regression":
    st.write("""
        ## **Simple Linear Regression Model**

        """)
    SLR()
elif modelSelect_name == "Random Forest Regression":
    st.write("""
        ## **Random Forest Regression Model**

        """)
    RFR()
