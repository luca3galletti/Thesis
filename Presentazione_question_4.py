#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go 
import plotly.express as px
import pickle


# In[ ]:


@st.cache_data(show_spinner=False)  
def load_data():
    order_month = pd.read_csv('order_month4.csv')
    ordered_correlation = pd.read_csv('ordered_correlation4.csv')
    evaded_correlation = pd.read_csv('evaded_correlation4.csv')
    return order_month, ordered_correlation, evaded_correlation

order_month, ordered_correlation, evaded_correlation = load_data()


# In[ ]:


st.title("Studio delle variabili o fattori ambientali che influiscono nelle vendite in diverse aeree")
with st.sidebar:
    st.subheader("Filtri")

    all_units = pd.concat([
        ordered_correlation['UNITA_MISURA'],
        evaded_correlation['UNITA_MISURA'],
        order_month['UNITA_MISURA']
    ]).unique()

    selected_unit_order_month = st.multiselect(
        "Seleziona Unità di Misura (Solo per Dati Mensili)",
        options=all_units,
        default=['N']
    )

    all_countries = order_month['COUNTRY'].unique()  # Filter countries based on order_month

    selected_country_order_month = st.multiselect(
        "Seleziona Paese (Solo per Dati Mensili)",
        options=all_countries,
        default=[]
    )

def display_correlation_table(df, title, default_unit='N'):
    st.header(title)

    st.subheader("Top 5 Valori")
    st.table(df[df['UNITA_MISURA'] == default_unit].nlargest(5, "Correlation"))
    st.subheader("Bottom 5 Valori")
    st.table(df[df['UNITA_MISURA'] == default_unit].nsmallest(5, "Correlation"))

display_correlation_table(ordered_correlation, "Correlazione tra Temperatura e Quantità Ordinata")
display_correlation_table(evaded_correlation, "Correlazione tra Temperatura e Quantità Evasa")

order_month_filtered = order_month[
    (order_month['UNITA_MISURA'].isin(selected_unit_order_month)) &
    (order_month['COUNTRY'].isin(selected_country_order_month))
]
st.header("Dati Mensili per Ordini e Temperatura")
st.table(order_month_filtered)

