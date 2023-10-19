import streamlit as st

def calculate_variable_cost(engine_reserve):
    if engine_reserve:
        return (100 / 50) + (7.50 * 0.15)
    else:
        return (100 / 50) + (7.50 * 0.15) + (4.75 * 8)

def calculate_metrics(fly_hours, engine_reserve, insurance, hanger_tiedown, annual_inspection,
                      avionics_subs, annual_loan_payment, annual_taxes_registration):
    rental_cost_hr = 135.0
    break_even_hours = 77

    variable_cost_hour = calculate_variable_cost(engine_reserve)
    fixed_cost_year = insurance + hanger_tiedown + annual_inspection + avionics_subs + annual_loan_payment + annual_taxes_registration
    fixed_cost_month = fixed_cost_year / 12
    cost_to_break_even = (break_even_hours * variable_cost_hour) + fixed_cost_year
    cost_to_fly_hours = (fly_hours * variable_cost_hour) + fixed_cost_year
    money_saved_or_lost = (fly_hours * rental_cost_hr) - cost_to_fly_hours

    return {
        "Total Variable Cost per Hour": variable_cost_hour,
        "Fixed Cost per Month": fixed_cost_month,
        "Total Fixed Cost per Year": fixed_cost_year,
        "Total Cost to Break Even": cost_to_break_even,
        "Cost to Fly Those Hours": cost_to_fly_hours,
        "Money Saved or Lost by Buying": money_saved_or_lost
    }

def main():
    st.set_page_config(page_title="Aviation Cost Calculator", page_icon="✈️", layout="wide")

    st.sidebar.image("cologne.png", use_column_width=True, caption="My Logo")

    st.sidebar.markdown("### Operating Costs (/hour)")
    fuel = st.sidebar.number_input("Fuel ($/hour)", value=38.0, step=1.0)
    oil_changes = st.sidebar.number_input("Oil Changes/Oil Adds ($/hour)", value=3.13, step=0.01)
    engine_reserve = st.sidebar.checkbox("Engine Reserve")

    st.sidebar.markdown("### Ownership Costs (/Year)")
    insurance = st.sidebar.number_input("Insurance ($/year)", value=1200.0, step=1.0)
    hanger_tiedown = st.sidebar.number_input("Hanger/Tiedown ($/year)", value=600.0, step=1.0)
    annual_inspection = st.sidebar.number_input("Annual Inspection ($/year)", value=1500.0, step=1.0)
    avionics_subs = st.sidebar.number_input("Avionics Database Subscriptions ($/year)", value=500.0, step=1.0)
    annual_loan_payment = st.sidebar.number_input("Annual Loan Payment ($/year)", value=3090.0, step=1.0)
    annual_taxes_registration = st.sidebar.number_input("Annual Taxes and Registration ($/year)", value=255.0, step=1.0)

    fly_hours = 77

    selected_calculation = st.selectbox("Select Calculation", [
        "Total Variable Cost per Hour",
        "Fixed Cost per Month",
        "Total Fixed Cost per Year",
        "Total Cost to Break Even",
        "Cost to Fly Those Hours",
        "Money Saved or Lost by Buying",
    ])

    metrics = calculate_metrics(fly_hours, engine_reserve, insurance, hanger_tiedown,
                                 annual_inspection, avionics_subs, annual_loan_payment, annual_taxes_registration)

    st.write(f"Selected Calculation: {selected_calculation}")
    st.write(f"{selected_calculation}: {metrics[selected_calculation]}")

if __name__ == '__main__':
    main()
