#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st


# In[ ]:


ordered = pd.read_csv('max_month_ordered.csv')
evaded = pd.read_csv('max_month_evaded.csv')
delta = pd.read_csv('max_month_delta.csv')


# In[ ]:


st.sidebar.title("Filters")

all_units = pd.concat([ordered['UNITA_MISURA'], evaded['UNITA_MISURA'], delta['UNITA_MISURA']]).unique()
selected_unit = st.sidebar.multiselect("Seleziona Unità di Misura", options=all_units, default=all_units)

all_countries = pd.concat([ordered['COUNTRY'], evaded['COUNTRY'], delta['COUNTRY']]).unique()
selected_country = st.sidebar.multiselect("Seleziona Paese", options=all_countries, default=all_countries)

ordered_filtered = ordered[(ordered['COUNTRY'].isin(selected_country)) & (ordered['UNITA_MISURA'].isin(selected_unit))]
evaded_filtered = evaded[(evaded['COUNTRY'].isin(selected_country)) & (evaded['UNITA_MISURA'].isin(selected_unit))]
delta_filtered = delta[(delta['COUNTRY'].isin(selected_country)) & (delta['UNITA_MISURA'].isin(selected_unit))]

st.title("Periodo dell'anno in cui ci sono più ordini")

st.header("Mese con la Quantità Ordinata più elevata")
st.table(ordered_filtered)

st.header("Mese con la Quantità Evasa più elevata")
st.table(evaded_filtered)

st.header("Mese con il Delta Ordini più elevato")
st.table(delta_filtered)

