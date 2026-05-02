#finance.py: Houses the Class A/B logic and the Black-Scholes code.


def calculate_ga_cost(mwh, ga_class="B", pdf=0.0, rate_b=60.0):
    """Calculates Global Adjustment based on Ontario consumer class."""
    if ga_class == "B":
        return mwh * rate_b
    # Simplified Class A logic
    provincial_pool = 1e9 / 12  # Estimated monthly pool
    return pdf * provincial_pool