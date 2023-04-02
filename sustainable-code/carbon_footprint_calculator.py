# Carbon footprint calculator

import csv

# Emissions factors (kg CO2e/unit)
ELECTRICITY_GRID_EMISSIONS = 0.000645  # kg CO2e/kWh
NATURAL_GAS_EMISSIONS = 0.0053  # kg CO2e/kWh
OIL_EMISSIONS = 0.00677  # kg CO2e/kWh
AVG_COMMUTE_EMISSIONS = 0.404  # kg CO2e/mile
AVG_FLIGHT_EMISSIONS = 0.217  # kg CO2e/mile
AVG_MEAT_EMISSIONS = 14.6  # kg CO2e/kg
AVG_VEGETABLE_EMISSIONS = 2.0  # kg CO2e/kg

# Open the CSV file
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    for row in csvreader:
        name = row[0]
        age = int(row[1])
        income = int(row[2])
        electricity_usage = float(row[3])
        natural_gas_usage = float(row[4])
        oil_usage = float(row[5])
        commute_miles = float(row[6])
        flight_miles = float(row[7])
        meat_consumption = float(row[8])
        vegetable_consumption = float(row[9])

        # Calculate emissions for each category
        electricity_emissions = electricity_usage * ELECTRICITY_GRID_EMISSIONS
        natural_gas_emissions = natural_gas_usage * NATURAL_GAS_EMISSIONS
        oil_emissions = oil_usage * OIL_EMISSIONS
        commute_emissions = commute_miles * AVG_COMMUTE_EMISSIONS
        flight_emissions = flight_miles * AVG_FLIGHT_EMISSIONS
        meat_emissions = meat_consumption * AVG_MEAT_EMISSIONS
        vegetable_emissions = vegetable_consumption * AVG_VEGETABLE_EMISSIONS

        # Calculate total emissions
        total_emissions = electricity_emissions + natural_gas_emissions + oil_emissions + commute_emissions + \
                          flight_emissions + meat_emissions + vegetable_emissions
        print(total_emissions)
