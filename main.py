import streamlit as st
from src.utils import initialize_project, add_sidebar_branding, add_sidebar_footer

# 1. Setup Page Configuration
st.set_page_config(page_title="IESO Digital Twin", layout="wide")

# Initialize folders and add top-level branding (Contact Info)
initialize_project()
add_sidebar_branding()

# 2. Define the Landing Page (Home)
def show_landing_page():
    st.title("Welcome to the IESO Energy Hedging Tool")
    st.markdown("---")

    st.markdown("""
    ### **Project Purpose**
    This tool acts as a **Financial Digital Twin** for Ontario industrial energy consumers. It allows you to:
    *   **Ingest Data:** Scrape real-time and historical price data from the IESO.
    *   **Simulate Risk:** Use the **Ornstein-Uhlenbeck** model to forecast price volatility.
    *   **Strategy Design:** Price Energy Caps and Collars using Black-Scholes to protect your budget.

    ### **How to Get Started**
    Use the sidebar on the left to navigate through the project phases:
    0.  **Project Charter:** Overview of goals, milestones, and stakeholders.
    1.  **Market Data:** Fetch and clean the latest IESO CSV reports.
    2.  **Hedging Strategy:** Calculate premiums and visualize your "Hedged vs. Unhedged" payoff.
    3.  **Simulations:** Run Monte Carlo paths to see potential future costs.
    """)
    
    st.sidebar.info("Select a module above to begin.")

# 3. Define Navigation Logic
pages = {
    "Overview": [
        st.Page(show_landing_page, title="Home", icon="🏠"),
        st.Page("pages/0_project_charter.py", title="Project Charter", icon="📜"),
        st.Page("pages/4_value_chain.py", title="Energy Value Chain", icon="⚡"),
    ],
    "Tools": [
        st.Page("pages/1_market_data.py", title="Market Data", icon="📊"),
        st.Page("pages/2_hedging_strategy.py", title="Hedging Strategy", icon="💰"),
        st.Page("pages/3_simulations.py", title="Simulations", icon="📈"),
    ]
}

# Run Navigation
pg = st.navigation(pages)
pg.run()

# 4. Add footer branding (Philosophical Insights below navigation)
add_sidebar_footer()