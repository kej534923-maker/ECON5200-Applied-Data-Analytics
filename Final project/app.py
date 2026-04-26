import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="IMF Crisis Dashboard", layout="wide")
st.title("IMF Crisis Early Warning Dashboard")

st.sidebar.header("Threshold Control")

threshold = st.sidebar.slider(
    "Crisis probability threshold",
    min_value=0.01, max_value=0.99, value=0.88, step=0.01
)

actual_crises = 14

if threshold >= 0.88:
    flagged, tp, fn = 5, 2, 12
elif threshold >= 0.14:
    flagged, tp, fn = 25, 10, 4
else:
    flagged, tp, fn = 48, 13, 1

recall = tp / actual_crises

st.subheader("Model Results")

col1, col2, col3 = st.columns(3)
col1.metric("Countries Flagged", flagged)
col2.metric("Crises Caught", tp)
col3.metric("Recall", f"{recall:.2%}")

st.markdown(f"""
At threshold **{threshold:.2f}**, the model flags **{flagged}** countries,
detects **{tp} out of {actual_crises}** crises, and misses **{fn}** crises.
""")

st.subheader("Counterfactual Scenario")

st.write(f"""
If the threshold is set to **{threshold:.2f}**, the expected recall becomes **{recall:.2%}**.
Lower thresholds increase detection but require more missions.
""")

taus = np.array([0.03, 0.14, 0.88])
costs = np.array([50, 200, 600])

fig = go.Figure()
fig.add_trace(go.Scatter(x=taus, y=costs, mode="lines+markers"))
fig.add_vline(x=threshold)

fig.update_layout(
    title="Expected Cost vs Threshold",
    xaxis_title="Threshold",
    yaxis_title="Cost ($B)"
)

st.plotly_chart(fig, use_container_width=True)
