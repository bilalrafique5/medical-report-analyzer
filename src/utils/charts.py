# src/utils/charts.py
import streamlit as st
import plotly.graph_objects as go
from ..utils.normal_ranges import NORMAL_RANGES

def show_value_vs_range(name, value):
    """
    Simple Plotly gauge-style bar comparing value to normal range.
    """
    if name not in NORMAL_RANGES:
        st.write(f"{name}: {value}")
        return
    r = NORMAL_RANGES[name]
    low, high = r["low"], r["high"]
    unit = r.get("unit","")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': f"{name.title()} ({unit})"},
        gauge={'axis': {'range': [0, max(high*1.5, value*1.2)]},
               'steps': [
                   {'range': [0, low], 'color': "lightblue"},
                   {'range': [low, high], 'color': "lightgreen"},
                   {'range': [high, max(high*1.5, value*1.2)], 'color': "salmon"}
               ],
               'threshold': {'line': {'color': "red", 'width': 4}, 'value': value}
              }
    ))
    st.plotly_chart(fig, use_container_width=True)
