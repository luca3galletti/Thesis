#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go


# In[ ]:


with open('mappa_Q5.pkl', 'rb') as f:
    fig = pickle.load(f)


# In[ ]:


max_orders = pd.read_csv('max_orders_by_country.csv')
top_countries_ordered = pd.read_csv('top_countries_ordered5.csv')
top_countries_evaded = pd.read_csv('top_countries_evaded5.csv')
top5_ordered = pd.read_csv('top5_ordered5.csv')
top5_evaded = pd.read_csv('top5_evasa5.csv')
top5_delta = pd.read_csv('top5_delta5.csv')


# In[ ]:


st.title("Distruzione delle famiglie nei distinti paesi")

st.sidebar.title("Filtri")

relevant_country_dfs = [max_orders, top5_ordered, top5_evaded, top5_delta]
all_countries = sorted(pd.concat([df['COUNTRY'] for df in relevant_country_dfs if 'COUNTRY' in df.columns]).unique())
selected_countries = st.sidebar.multiselect("Select Countries", all_countries, default=all_countries)

def clean_descrizione1(df):
    valid_descrizione1 = df['DESCRIZIONE1'].str.contains(r'^[A-Za-z]+$', regex=True)
    return df[valid_descrizione1]

top_countries_ordered_clean = clean_descrizione1(top_countries_ordered)
top_countries_evaded_clean = clean_descrizione1(top_countries_evaded)

all_descrizioni1 = sorted(
    pd.concat([
        top_countries_ordered_clean['DESCRIZIONE1'], 
        top_countries_evaded_clean['DESCRIZIONE1']
    ]).unique()
)

selected_desc1 = st.sidebar.multiselect(
    "Seleziona Famiglia Prodotto",
    options=all_descrizioni1,
    default=all_descrizioni1
)

top_countries_ordered_filtered = top_countries_ordered_clean[
    (top_countries_ordered_clean['COUNTRY'].isin(selected_countries)) &
    (top_countries_ordered_clean['DESCRIZIONE1'].isin(selected_desc1))
]

top_countries_evaded_filtered = top_countries_evaded_clean[
    (top_countries_evaded_clean['COUNTRY'].isin(selected_countries)) &
    (top_countries_evaded_clean['DESCRIZIONE1'].isin(selected_desc1))
]

def show_max_orders():
    filtered_max_orders = max_orders[max_orders['COUNTRY'].isin(selected_countries)]
    st.header("Famiglie di prodotto più ordinate per paese")
    st.dataframe(filtered_max_orders.style.hide(axis="index"))

show_max_orders()

def show_top5_ordered():
    filtered_top5_ordered = top5_ordered[top5_ordered['COUNTRY'].isin(selected_countries)]
    st.header("Top 5 Famiglie di prodotti per quantità ordinata")
    st.dataframe(filtered_top5_ordered.style.hide(axis="index"))

show_top5_ordered()

def show_top5_evaded():
    filtered_top5_evaded = top5_evaded[top5_evaded['COUNTRY'].isin(selected_countries)]
    st.header("Top 5 Famiglie di prodotti per quantità evasa")
    st.dataframe(filtered_top5_evaded.style.hide(axis="index"))

show_top5_evaded()

def show_top5_delta():
    filtered_top5_delta = top5_delta[top5_delta['COUNTRY'].isin(selected_countries)]
    st.header("Top 5 Famiglie di prodotti per delta ordini")
    st.dataframe(filtered_top5_delta.style.hide(axis="index"))

show_top5_delta()

st.header("Top 5 Paesi per Quantità Ordinata")
st.dataframe(top_countries_ordered_filtered.style.hide(axis="index"))

st.header("Top 5 Paesi per Quantità Evasa")
st.dataframe(top_countries_evaded_filtered.style.hide(axis="index"))

st.header("Mappa distribuzione ordini per paese")
st.plotly_chart(fig)

