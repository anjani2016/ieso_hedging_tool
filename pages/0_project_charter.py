import streamlit as st
from src.utils import initialize_project

st.title("📜 Project Charter: Energy Hedging Digital Twin")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("1. Executive Summary")
    st.write("""
    This project aims to develop a **Financial Digital Twin** for Ontario-based industrial energy consumers. 
    By leveraging historical data from the IESO (Independent Electricity System Operator), the tool provides 
    transparency into market volatility and enables the design of robust hedging strategies (Caps, Collars, and Swaps).
    """)

    st.header("2. Business Objectives")
    st.markdown("""
    - **Risk Mitigation:** Protect against spikes in the Hourly Ontario Energy Price (HOEP).
    - **Budget Predictability:** Provide mean-reverting simulations to forecast monthly energy spend.
    - **Strategic Decision Making:** Compare unhedged market exposure against various derivative strategies.
    """)

with col2:
    st.header("3. Stakeholders")
    st.info("""
    - **Project Sponsor:** Centauri Research
    - **Primary Users:** Energy Managers, CFOs, Risk Analysts
    - **Data Provider:** IESO (Public Reports)
    """)

st.header("4. Key Milestones")
st.table({
    "Phase": ["Data Ingestion", "Risk Modeling", "Strategy Engine", "Deployment"],
    "Status": ["✅ Complete", "✅ In Progress", "⏳ Pending", "⏳ Pending"],
    "Target Date": ["2026-03", "2026-04", "2026-05", "2026-06"]
})

st.markdown("---")
st.info("This charter serves as the 'Source of Truth' for project goals and scope.")
