# src/utils.py
import logging
import streamlit as st
import os

def add_sidebar_branding():
    """Adds logo and contact info to the Streamlit sidebar."""
    logo_path = "data/assets/CR_logo.png"
    
    with st.sidebar:
        # Check if the logo exists to prevent errors
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
        else:
            st.warning("Logo file not found in data/assets/")
        
        st.markdown("---")
        st.markdown("### **Contact & Support**")
        st.markdown("[📧 Email Support](mailto:anjani@centauri-research.com)")
        st.markdown("[🌐 Official Website](https://centauri-research.com/)")
        st.markdown("---")

def initialize_project():
    """Creates the necessary folder structure automatically."""
    folders = [
        'data/raw', 
        'data/processed', 
        'data/assets', 
        'logs'
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Setup simple logging for the audit trail
    logging.basicConfig(
        filename='logs/project_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Project directories initialized.")

def format_currency(value):
    return f"${value:,.2f}"