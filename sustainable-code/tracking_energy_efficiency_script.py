# Energy Efficiency Tracker with Input Checks

import datetime

# Constants
KWH_TO_CO2_FACTOR = 0.000688  # CO2 emissions per kWh in metric tons
MONTHS_IN_YEAR = 12

# Input data
electricity_use = []  # kWh of electricity used each month
gas_use = []  # Therms of natural gas used each month

# Helper functions
def calculate_emissions(electricity_use, gas_use):
    """
    Calculate the total CO2 emissions for a given month based on electricity and natural gas use.
    """
    electricity_emissions = electricity_use * KWH_TO_CO2_FACTOR
    gas_emissions = gas_use * 0.0053  # CO2 emissions per therm of natural gas in metric tons
    total_emissions = electricity_emissions + gas_emissions
    return total_emissions

def calculate_average_emissions(data):
    """
    Calculate the average monthly CO2 emissions for a given data set.
    """
    total_emissions = sum(data)
    average_emissions = total_emissions / len(data)
    return average_emissions

# Input loop
while True:
    electricity = input("Enter the kWh of electricity used this month (or 'done' to exit): ")
    if electricity.lower() == "done":
        break
    try:
        electricity_use.append(float(electricity))
    except ValueError:
        print("Invalid input. Please enter a number for electricity usage.")
        continue
    gas = input("Enter the therms of natural gas used this month: ")
    try:
        gas_use.append(float(gas))
    except ValueError:
        print("Invalid input. Please enter a number for gas usage.")
        continue
    date_str = input("Enter the date of this reading (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid input. Please enter the date in the format YYYY-MM-DD.")
        continue

# Calculate emissions and efficiency
if electricity_use and gas_use:
    emissions_data = []
    for i in range(len(electricity_use)):
        emissions = calculate_emissions(electricity_use[i], gas_use[i])
        emissions_data.append(emissions)
    average_emissions = calculate_average_emissions(emissions_data)
    annual_emissions = average_emissions * MONTHS_IN_YEAR

    # Output results
    print(f"\nAverage monthly CO2 emissions: {average_emissions:.2f} metric tons")
    print(f"Annual CO2 emissions: {annual_emissions:.2f} metric tons")
else:
    print("No data entered. Please try again.")    
