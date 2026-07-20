import streamlit as st
import pandas as pd

def save_prediction(result):

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(result)

def get_history():

    if "history" not in st.session_state:
        st.session_state.history = []

    return pd.DataFrame(st.session_state.history)