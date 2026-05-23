
# Project structure
```
ieso_hedging_tool/
├── .streamlit/             # Streamlit configuration (theme, port)
├── data/                   
│   ├── raw/                # Original IESO CSV files
│   ├── processed/          # Cleaned data ready for simulation
│   └── assets/             # Logos or static images
├── src/                    # The "Engine Room" (Internal Logic)
│   ├── __init__.py         # Makes this folder a package
│   ├── scraper.py          # Step 1: IESO Data retrieval logic
│   ├── models.py           # Step 2: OU Process & Simulation classes
│   ├── finance.py          # Step 3: Black-Scholes & GA Logic
│   └── utils.py            # General helpers (loggers, date parsers)
├── pages/                  # Streamlit Views (Presentation Layer)
│   ├── 1_📊_Market_Data.py
│   ├── 2_📈_Simulations.py
│   └── 3_💰_Hedging_Strategy.py
|
│
├── database/
│   ├── schema/
│   │   ├── 01_dimensions.sql      # Tables for Grid Nodes/Zones
│   │   ├── 01_dimensions.sql      # Tables for Grid Nodes/Zones
│   │   ├── 01_dimensions.sql      # Tables for Grid Nodes/Zones
│   │   ├── 01_dimensions.sql      # Tables for Grid Nodes/Zones
│   │   └── 02_hypertables.sql      # Fact tables and TimescaleDB setups
│   │
│   ├── queries/
│   │   ├── fetch_historical_volatility.sql
│   │   ├── upsert_5min_demand.sql
│   │   └── upsert_5min_lmp.sql 
│   │
│   └── views/
│       └── 01_hourly_rollups.sql   # Continuous aggregations
│
├── engines/
│   ├── __init__.py
│   ├── ingestion_peakhours.py     # peakhours ingestion    
│   ├── db_manager.py              # The database utility script
│   └── forecasting.py             # Your ML / Risk engine
|
└── main.py                 # Landing page & App Entry Point


```




