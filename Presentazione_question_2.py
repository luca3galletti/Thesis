#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st


# In[ ]:


top_delta = pd.read_csv('top_delta_table2.csv')
sorted_table = pd.read_csv('top_unit_delta_table2.csv')
delta = pd.read_csv('filtered_table2.csv')


# In[ ]:


st.sidebar.title("Filters")

selected_units = st.sidebar.multiselect(
    "Seleziona Unità di Misura",
    options=sorted_table['UNITA_MISURA'].unique(),
    default=sorted_table['UNITA_MISURA'].unique()
)

selected_countries = st.sidebar.multiselect(
    "Seleziona Paese",
    options=delta['COUNTRY'].unique(),
    default=delta['COUNTRY'].unique()
)

sorted_table_filtered = sorted_table[sorted_table['UNITA_MISURA'].isin(selected_units)]
delta_filtered_country = delta[delta['COUNTRY'].isin(selected_countries)]
delta_filtered = delta_filtered_country[delta_filtered_country['UNITA_MISURA'].isin(selected_units)]

st.title('Paesi con delta ordini maggiore')

st.header("Top 10 paesi per Delta Ordini")
st.table(top_delta)
st.text("Senza distinzione in base all'unità di misura della quantità")

st.header("Top 10 paesi per Delta Ordini in base all'unità di misura")
st.table(sorted_table_filtered) 

st.header("Delta Ordini associato al numero di macchine per paese")
st.table(delta_filtered)

