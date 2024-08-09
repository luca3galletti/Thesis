#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go


# In[ ]:


with open('mappa.pkl', 'rb') as f:
    fig = pickle.load(f)


# In[ ]:


delta = pd.read_csv('top_3_delta_country.csv')


# In[ ]:


st.sidebar.title("Filters")

selected_countries = st.sidebar.multiselect(
    "Seleziona Paese", 
    options=delta['COUNTRY'].unique(), 
    default=delta['COUNTRY'].unique()
)

filtered_delta = delta[delta['COUNTRY'].isin(selected_countries)]

st.title('Mappa di distribuzione dei ricambi per paese')
st.plotly_chart(fig) 

st.subheader("Top 3 prodotti per Delta Ordini in ogni paese")
st.table(filtered_delta)

