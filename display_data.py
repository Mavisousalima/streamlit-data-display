import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from time import sleep

from settings import collection


fig = make_subplots(specs=[[{"secondary_y": True}]])

@st.cache_data(ttl=60)
def get_data():
    data = []
    docs = collection.find().sort('timestamp', 1)
    for doc in docs:
        data.append(doc)
    return data


"""
This script uses Streamlit to create a real-time line chart that displays the values stored in the Firestore database. 
It uses Plotly to create the chart, and the 'get_data' function uses Streamlit's caching feature to only retrieve 
the data from the database once per minute, reducing the number of database requests.
"""
while True:
    data = get_data()
    x = [d['timestamp'] for d in data]
    y = [d['value'] for d in data]

    fig.add_trace(
        go.Scatter(x=x, y=y, mode='lines', name='Value'),
        secondary_y=False,
    )

    fig.update_layout(title='Real-time Data')
    st.plotly_chart(fig, use_container_width=True)
    sleep(60)
