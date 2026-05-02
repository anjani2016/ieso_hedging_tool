import streamlit as st
from src.utils import initialize_project, add_sidebar_branding

# 1. Setup Page Configuration


st.set_page_config(page_title="IESO Digital Twin", layout="wide")

# Initialize folders and add branding
initialize_project()
add_sidebar_branding() 

# ... rest of your code ...
# 2. Run the Initialization Helper
# This creates your /data and /logs folders automatically
initialize_project()

# 3. Landing Page UI
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
1.  **Market Data:** Fetch and clean the latest IESO CSV reports.
2.  **Simulations:** Run Monte Carlo paths to see potential future costs.
3.  **Hedging Strategy:** Calculate premiums and visualize your "Hedged vs. Unhedged" payoff.
""")

st.sidebar.info("Select a module above to begin.")