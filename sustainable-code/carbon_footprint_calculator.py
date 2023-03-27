

def get_footprint_comment(total_emissions):
    """Returns a colored comment based on the given carbon footprint value."""
    if total_emissions < 400:
        comment = "\033[32mYour carbon footprint is very low! Keep up the good work.\033"
    elif total_emissions < 1200:
        comment = "\033[32mYour carbon footprint is low, but there is still room for improvement." + "\nConsider reducing your energy consumption and transportation emissions."
    elif total_emissions < 1600:
        comment = "\033[33mYour carbon footprint is average, but there is room for improvement." + "\nConsider reducing your meat consumption, choosing sustainable transportation, and using energy-efficient appliances.\033"
    else:
        comment = "\033[31mYour carbon footprint is high. You should consider reducing your emissions.\033"

    # Print results
    print(f"Your monthly carbon footprint is {total_emissions:.2f} kg CO2e.")
    print(comment)


def main():
    # Emissions factors (kg CO2e/unit)
    emissions_factors = {
        "electricity": 0.000645,  # kg CO2e/kWh
        "natural gas": 0.0053,  # kg CO2e/kWh
        "oil": 0.00677,  # kg CO2e/kWh
        "commute": 0.404,  # kg CO2e/mile
        "flight": 0.217,  # kg CO2e/mile
        "meat": 14.6,  # kg CO2e/kg
        "vegetable": 2.0  # kg CO2e/kg
    }

    # Prompt user for input
    inputs = {}
    for category, factor in emissions_factors.items():
        while True:
            try:
                usage = float(input(f"Enter your monthly {category} {'consumption in kg' if category in ('meat', 'vegetable') else ('usage in kWh' if category in ('electricity', 'natural gas', 'oil') else 'distance in miles')}: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                print("\033[31mInvalid input. Please enter a number.\033[0m")
        inputs[category] = usage * factor

    # Calculate total emissions
    total_emissions = sum(inputs.values())

    get_footprint_comment(total_emissions)


if __name__ == '__main__':
    main()
