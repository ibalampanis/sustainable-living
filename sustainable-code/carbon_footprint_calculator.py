import matplotlib.pyplot as plt
import numpy as np

def get_user_usage(category: str) -> float:
    '''Asks the user their usage in an emission category
    
    Parameters:
        category: the type of emission

    Returns:
        usage: a float number of user's input
    '''
    prompt = {'electricity': 'usage in kWh',
              'natural gas': 'usage in kWh',
              'oil': 'usage in kWh',
              'commute':'distance in miles',
              'flight': 'distance in miles',
              'meat': 'consumption in kg',
              'vegetable': 'consumption in kg'
              }

    while True:
        try:
            usage = float(input(
                f"Enter your monthly {category} {prompt[category]}: "))
            return usage
        except ValueError:
            print("\033[31mInvalid input. Please enter a number.\033[0m")


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


def get_chart(usage):
    """Plots a donut chart of the usage of each emission category."""
    categories = list(usage.keys())
    values = list(usage.values())
    colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#4CAF50', '#2196F3']
    fig, ax1 = plt.subplots()
    ax1.pie(values, colors=colors, startangle=90, counterclock=False, autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.05)
    ax1.axis('equal')
    ax1.set_title("Emission Categories")
    ax1.legend(categories, loc="best")
    plt.show()



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
    cat_usage = {}
    for category, factor in emissions_factors.items():
        usage = get_user_usage(category)
        cat_usage[category] = usage
        inputs[category] = usage * factor

    # Calculate total emissions
    total_emissions = sum(inputs.values())


    get_chart(cat_usage)
    get_footprint_comment(total_emissions)

if __name__ == '__main__':
    main()
