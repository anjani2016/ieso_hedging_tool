import streamlit as st
from src.utils import initialize_project
import streamlit.components.v1 as components

st.title("📜 Project Charter: Energy Hedging Digital Twin")
st.markdown("---")
html_content = """
# Project Charter

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Digital Twin | Business Summary 2026</title>
    <style>
        :root {
            --primary: #2c3e50;
            --accent: #e67e22;
            --danger: #c0392b;
            --bg: #f4f7f6;
        }
        body { font-family: 'Segoe UI', sans-serif; background: var(--bg); padding: 20px; line-height: 1.6; }
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        header { border-bottom: 4px solid var(--primary); margin-bottom: 25px; padding-bottom: 10px; }
        h2 { color: var(--primary); border-left: 5px solid var(--accent); padding-left: 10px; margin-top: 30px; }
        .status-table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        .status-table th, .status-table td { padding: 12px; border: 1px solid #ddd; text-align: left; }
        .status-table th { background: #f8f9fa; }
        .error-panel { background: #fdf2f2; border: 1px solid var(--danger); padding: 20px; border-radius: 5px; margin-top: 20px; }
        .error-panel h3 { color: var(--danger); margin-top: 0; }
        .badge { display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold; }
        .badge-complete { background: #d4edda; color: #155724; }
        .badge-progress { background: #fff3cd; color: #856404; }
        .badge-pending { background: #e2e3e5; color: #383d41; }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Executive Project Charter: Financial Digital Twin</h1>
        <p>Strategic Risk Modeling for Ontario Industrial Energy Consumers (Market Renewal Era)</p>
    </header>

    <h2>1. Executive Summary</h2>
    <p>This project develops a high-fidelity <strong>Financial Digital Twin</strong> to navigate Ontario's post-2025 Market Renewal environment. By transitioning from HOEP to <strong>Locational Marginal Pricing (LMP)</strong>, the tool enables industrial users to simulate and execute hedging strategies (Caps, Collars, Swaps) to stabilize energy OPEX.</p>

    <h2>2. Business Objectives</h2>
    <ul>
        <li><strong>Risk Mitigation:</strong> Protection against nodal price spikes exceeding $200/MWh.</li>
        <li><strong>Budget Predictability:</strong> Mean-reverting stochastic simulations for 12-month fiscal planning.</li>
        <li><strong>Strategy Engine:</strong> Evaluating "Hedge Effectiveness" against real-time congestion costs.</li>
    </ul>

    <h2>3. Stakeholders</h2>
    <p><strong>Project Sponsor:</strong> Centauri Research | <strong>Primary Users:</strong> CFOs, Energy Managers | <strong>Data:</strong> IESO Public Reports & API</p>


    <h2>4. Mathematical Modelling</h2>
    <p> The simulation engine uses an Ornstein–Uhlenbeck (OU) mean‑reverting stochastic model to represent electricity prices, 
    which naturally spike during grid stress and revert toward structural equilibrium.
      The OU process captures three core dynamics:
    </p>
    <ul>
        <li><strong>Long-term Mean (μ):</strong> The system's equilibrium HOEP level.</li>
        <li><strong>Reversion Speed (θ):</strong> How quickly prices snap back after volatility events.</li>
        <li><strong>Volatility (σ):</strong> The magnitude of weather‑ and congestion‑driven shocks.</li>
    </ul>
    <p>This mean‑reverting framework ensures the tool reflects physical grid behavior, not equity‑style upward drift, 
    and provides a realistic foundation for hedge valuation, Greeks analysis, and Monte Carlo risk scenarios.</p>

    <h2>5. Project Milestones (2026)</h2>
    <table class="status-table">
        <thead>
            <tr><th>Phase</th><th>Status</th><th>Target Date</th></tr>
        </thead>
        <tbody>
            <tr><td>Data Ingestion</td><td><span class="badge badge-complete">✅ Complete</span></td><td>2026-03</td></tr>
            <tr><td>Risk Modeling (Greeks)</td><td><span class="badge badge-progress">🟡 In Progress</span></td><td>2026-04</td></tr>
            <tr><td>Strategy Engine</td><td><span class="badge badge-pending">⏳ Pending</span></td><td>2026-05</td></tr>
            <tr><td>Deployment</td><td><span class="badge badge-pending">⏳ Pending</span></td><td>2026-06</td></tr>
        </tbody>
    </table>

    <!-- SECTION 6: THE MISSING LINKS -->
    <div class="error-panel">
        <h3>5. Strategic Vulnerabilities (Missing Logic Links)</h3>
        <p>Current analysis is <strong>non-predictive</strong> and prone to error due to the absence of the following critical physical-financial links:</p>
        <ul>
            <li><strong>Missing Nodal Correlation (Basis Risk):</strong> The model currently relies on Zonal Averages. Without nodal-specific transmission data, <strong>Delta (&Delta;)</strong> calculations will misrepresent the actual cost at the client's facility by 15-30% during congestion events.</li>
            <li><strong>Missing Atmospheric Physics (Quantity Risk):</strong> The hedge does not currently ingest <strong>Wind Hub-Height</strong> or <strong>Solar Irradiance</strong> data. This leads to "Quantity Errors" where the volume hedged does not match the volume generated, potentially resulting in forced market buy-backs at peak prices.</li>
            <li><strong>Linearity Bias (Gamma Risk):</strong> The model assumes price changes are linear. In the Ontario grid, transmission "Shadow Prices" create <strong>Convexity</strong>; once a line hits capacity, the price accelerates exponentially. Without SCED-logic integration, <strong>Gamma (&Gamma;)</strong> is severely underestimated.</li>
            <li><strong>DART Spread Omission:</strong> Lack of differentiation between Day-Ahead and Real-Time settlement creates a "Slippage Gap" in P&L reporting, as industrial hedges often settle against different time-intervals than physical delivery.</li>
        </ul>
    </div>

    <footer style="margin-top: 30px; font-size: 0.8em; text-align: center; color: #777;">
        &copy; 2026 Digital Twin Project  Strategic Framework
    </footer>
</div>

</body>
</html>

"""

components.html(html_content, height=1400, scrolling=True)

st.markdown("---")
st.info("This charter serves as the 'Source of Truth' for project goals and scope.")
