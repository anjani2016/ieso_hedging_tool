import streamlit as st
from src.models import EnergySimulator  # Absolute import from src

st.set_page_config(page_title="Simulation Engine")

st.title("OU Process Simulation")

# User Inputs for the Math Model
col1, col2 = st.columns(2)
with col1:
    mu = st.slider("Mean Price ($)", 20, 100, 35)
    theta = st.slider("Reversion Speed (Theta)", 0.01, 0.5, 0.1)
with col2:
    sigma = st.slider("Volatility (Sigma)", 1, 20, 5)

if st.button("Generate Price Paths"):
    sim = EnergySimulator(s0=40, mu=mu, theta=theta, sigma=sigma)
    paths = sim.run_monte_carlo()
    st.line_chart(paths)
    st.info("The price path shows mean reversion toward the target $mu$.")