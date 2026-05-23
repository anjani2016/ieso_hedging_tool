import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Ontario Energy Market Value Chain", layout="wide")

html_content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ontario Energy Market Summary | 2026</title>
    <style>
        :root {
            --primary: #2c3e50;
            --secondary: #34495e;
            --accent: #3498db;
            --light: #ecf0f1;
            --border: #bdc3c7;
            --success: #27ae60;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--primary);
            background-color: #f4f7f6;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        header {
            border-bottom: 3px solid var(--accent);
            margin-bottom: 30px;
            padding-bottom: 10px;
        }

        h1 { margin: 0; color: var(--primary); font-size: 28px; }
        h2 { color: var(--accent); border-left: 5px solid var(--accent); padding-left: 15px; margin-top: 30px; font-size: 20px; }
        
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 0.9em;
        }

        th, td {
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid var(--border);
        }

        th { background-color: var(--light); color: var(--secondary); }

        .highlight-box {
            background-color: var(--light);
            padding: 20px;
            border-radius: 5px;
            border-left: 5px solid var(--success);
            margin: 15px 0;
        }

        .formula {
            background: #273746;
            color: #d5d8dc;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            margin: 10px 0;
        }

        .footer {
            margin-top: 40px;
            font-size: 0.8em;
            color: #7f8c8d;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Ontario Energy Market Value Chain & Hedging Brief</h1>
        <p>Strategic Overview: Physics, Regulation, and Financial Greeks</p>
    </header>

    <!-- 1. The Energy Value Chain -->
    <h2>1. Value Chain Players & Roles</h2>
    <table>
        <thead>
            <tr>
                <th>Tier</th>
                <th>Participants</th>
                <th>Primary Role</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Generators</strong></td>
                <td>OPG, Bruce Power, Wind/Solar IPPs</td>
                <td>Supply electrons via Nuclear, Hydro, Gas, and Renewables.</td>
            </tr>
            <tr>
                <td><strong>Transmitters</strong></td>
                <td>Hydro One</td>
                <td>Maintains high-voltage "Highways"; manages physical grid capacity.</td>
            </tr>
            <tr>
                <td><strong>Distributors (LDCs)</strong></td>
                <td>Toronto Hydro, Alectra</td>
                <td>"Last-mile" delivery. Non-profit on energy; profit on infrastructure.</td>
            </tr>
            <tr>
                <td><strong>Market Operator</strong></td>
                <td>IESO</td>
                <td>The "Air Traffic Controller." Balances 60Hz frequency and runs the auction.</td>
            </tr>
            <tr>
                <td><strong>Brokers/Devs</strong></td>
                <td>Brookfield, Aggregators</td>
                <td>Financial facilitators; help small projects reach market scale.</td>
            </tr>
        </tbody>
    </table>

    <!-- 2. Contracts and Purpose -->
    <h2>2. Pricing Contracts: Purpose & Protection</h2>
    <div class="grid">
        <div class="highlight-box">
            <strong>Fixed-Price CfDs (Bruce Power/IESO)</strong>
            <p>Protects the generator from price crashes. If Market < Contract, IESO pays the gap. If Market > Contract, Generator rebates the excess (clawback).</p>
        </div>
        <div class="highlight-box">
            <strong>Industrial Hedges (Class A Users)</strong>
            <p>Protects the consumer from price spikes. Uses Swaps/Options to cap energy costs during peak weather events.</p>
        </div>
    </div>

    <!-- 3. Price Setting -->
    <h2>3. Price Determination Logic</h2>
    <ul>
        <li><strong>LCOE (Levelized Cost):</strong> The average total cost to build/operate a plant. Used for long-term planning.</li>
        <li><strong>Spot Market Price:</strong> Set by the <strong>Marginal Generator</strong>. Usually Natural Gas. Every 5 minutes, the most expensive plant needed to meet demand sets the price for everyone.</li>
    </ul>

    <!-- 4. Price to Customer -->
    <h2>4. Regulatory Pricing (The OEB Layer)</h2>
    <p>The <strong>Ontario Energy Board (OEB)</strong> acts as a buffer between the volatile market and the consumer.</p>
    <div class="highlight-box" style="border-left-color: var(--accent);">
        <strong>Consumer Rate = Forecasted (Gen Costs + Global Adjustment + Delivery)</strong>
        <br><small>Discrepancies are held in "Variance Accounts" for future settlement.</small>
    </div>

    <!-- 5. Market Price Calculation -->
    <h2>5. The Nodal Price (LMP) Calculation</h2>
    <p>In the 2025 Market Renewal environment, every location has a unique price:</p>
    <div class="formula">
        LMP = System Energy Cost + Transmission Loss + Congestion Shadow Price
    </div>
    <ul>
        <li><strong>Congestion:</strong> The "premium" paid when a cheap path is full, forcing the IESO to use a local, expensive generator.</li>
        <li><strong>Futures Markets:</strong> Move based on anticipated grid "tightness," weather patterns (La Niña/El Niño), and Natural Gas forward curves.</li>
    </ul>

    <!-- 6. Hedging & Greeks -->
    <h2>6. The Energy Hedging Process (Greeks)</h2>
    <p>Unlike stocks, energy Greeks are driven by <strong>Weather & Physics</strong>:</p>
    <table>
        <thead>
            <tr>
                <th>Greek</th>
                <th>Energy Market Translation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Delta (&Delta;)</strong></td>
                <td>Sensitivity to Price/Demand. How value moves with a 100MW demand increase.</td>
            </tr>
            <tr>
                <td><strong>Vega (&nu;)</strong></td>
                <td>Sensitivity to Supply Volatility (e.g., how unpredictable wind speeds affect costs).</td>
            </tr>
            <tr>
                <td><strong>Theta (&Theta;)</strong></td>
                <td>Time decay of a hedge, often tied to seasonal reservoir levels (Hydrological Theta).</td>
            </tr>
            <tr>
                <td><strong>Gamma (&Gamma;)</strong></td>
                <td>Acceleration risk during "Grid Stress" (e.g., price jumping from $40 to $2000).</td>
            </tr>
        </tbody>
    </table>

    <div class="footer">
        <p>&copy; 2026 Energy Strategy Dashboard | Generated for Digital Twin Framework</p>
    </div>
</div>

</body>
</html>
"""

components.html(html_content, height=1400, scrolling=True)