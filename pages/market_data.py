import streamlit as st
import pandas as pd
from src.scraper import fetch_ieso_data, save_raw_data
from datetime import datetime
from src.utils import initialize_project, add_sidebar_branding

st.set_page_config(page_title="IESO Digital Twin", layout="wide")

# Initialize folders and add branding
initialize_project()
add_sidebar_branding() 

# ... rest of code ...

st.title("📊 IESO Market Data Ingestion")
st.markdown("Download and preview historical Hourly Ontario Energy Price (HOEP) data.")

# 1. User Inputs
with st.sidebar:
    st.header("Data Settings")
    selected_date = st.date_input("Select Month to Scrape", value=datetime(2026, 3, 1))
    year_month = selected_date.strftime("%Y%m")

# 2. Execution Button
if st.button(f"Fetch Data for {year_month}"):
    with st.spinner("Connecting to IESO Servers..."):
        data = fetch_ieso_data(year_month)
        
        if isinstance(data, pd.DataFrame):
            # Save the data to our local structure
            path = save_raw_data(data, year_month)
            
            st.success(f"Data successfully saved to {path}")
            
            # 3. Data Preview & Metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Average Price", f"${data['Ontario Price'].mean():.2f}")
            col2.metric("Max Price", f"${data['Ontario Price'].max():.2f}")
            col3.metric("Data Points", len(data))
            
            st.subheader("Raw Data Preview")
            st.dataframe(data, use_container_width=True)
            
            # Simple visualization of the month
            st.subheader("Price Trend")
            st.line_chart(data['Ontario Price'])
            
        else:
            st.error(f"Failed to retrieve data: {data}")

st.divider()

# ... (Scraper button logic remains the same) ...

# 3. Data Check & Preview
st.divider()
st.subheader("Current Session Data")

# We check if 'data' was successfully created in this session
if 'data' in locals() and isinstance(data, pd.DataFrame):
    st.dataframe(data, use_container_width=True)
    st.line_chart(data['Ontario Price'])
else:
    # This shows when the page first loads
    st.info("No data loaded for this session. Use the 'Fetch Data' button in the sidebar to begin.")

st.divider()
st.info("Note: The IESO reports are updated monthly. Ensure you are selecting a period with available public reports.")