# Carbon footprint calculator

# Emissions factors (kg CO2e/unit)
ELECTRICITY_GRID_EMISSIONS = 0.000645  # kg CO2e/kWh
NATURAL_GAS_EMISSIONS = 0.0053  # kg CO2e/kWh
OIL_EMISSIONS = 0.00677  # kg CO2e/kWh
AVG_COMMUTE_EMISSIONS = 0.404  # kg CO2e/mile
AVG_FLIGHT_EMISSIONS = 0.217  # kg CO2e/mile
AVG_MEAT_EMISSIONS = 14.6  # kg CO2e/kg
AVG_VEGETABLE_EMISSIONS = 2.0  # kg CO2e/kg

# Prompt user for input
electricity_usage = float(input("Enter your monthly electricity usage in kWh: "))
natural_gas_usage = float(input("Enter your monthly natural gas usage in kWh: "))
oil_usage = float(input("Enter your monthly oil usage in kWh: "))
commute_miles = float(input("Enter your monthly commute distance in miles: "))
flight_miles = float(input("Enter your monthly flight distance in miles: "))
meat_consumption = float(input("Enter your monthly meat consumption in kg: "))
vegetable_consumption = float(input("Enter your monthly vegetable consumption in kg: "))

# Calculate emissions for each category
electricity_emissions = electricity_usage * ELECTRICITY_GRID_EMISSIONS
natural_gas_emissions = natural_gas_usage * NATURAL_GAS_EMISSIONS
oil_emissions = oil_usage * OIL_EMISSIONS
commute_emissions = commute_miles * AVG_COMMUTE_EMISSIONS
flight_emissions = flight_miles * AVG_FLIGHT_EMISSIONS
meat_emissions = meat_consumption * AVG_MEAT_EMISSIONS
vegetable_emissions = vegetable_consumption * AVG_VEGETABLE_EMISSIONS

# Calculate total emissions
total_emissions = electricity_emissions + natural_gas_emissions + oil_emissions + commute_emissions + flight_emissions + meat_emissions + vegetable_emissions


def get_footprint_comment(total_emissions):
    """Returns a colored comment based on the given carbon footprint value."""

    if total_emissions < 400:
        comment = "\033[32mYour carbon footprint is very low! Keep up the good work.\033[0m"
    elif total_emissions < 1200:
        comment = "\033[32mYour carbon footprint is low, but there is still room for improvement."+"\nConsider reducing your energy consumption and transportation emissions.[0m"
    elif total_emissions < 1600:
        comment = "\033[33mYour carbon footprint is average, but there is room for improvement."+"\nConsider reducing your meat consumption, choosing sustainable transportation, and using energy-efficient appliances.\033[0m"
    else:
        comment = "\033[31mYour carbon footprint is high. You should consider reducing your emissions.\033[0m"

    # Print results
    print(f"Your monthly carbon footprint is {total_emissions:.2f} kg CO2e.")
    print(comment)

get_footprint_comment(total_emissions)