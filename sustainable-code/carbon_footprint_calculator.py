import matplotlib.pyplot as plt

def get_user_usage(category: str) -> float:
    """Ask the user their usage in an emission category.
    
    Arguments:
    category -- the type of emission

    Returns:
    a float number of user's input
    """
    prompt = {'electricity': 'usage in kWh',
              'natural gas': 'usage in kWh',
              'oil': 'usage in kWh',
              'commute': 'distance in miles',
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

def get_footprint_comment(total_emissions) -> None:
    """Return a colored comment based on the given carbon footprint value.
    
    Arguments:
    total_emissions -- the sum of all the given emissions
    """
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

def get_chart(usage: dict[str, float]) -> None:
    """Plot a donut chart of the usage of each emission category.
    
    Arguments:
    usage -- dictionary where keys are the categories and values are each category's usage
    """
    categories = list(usage.keys())
    values = list(usage.values())
    colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#4CAF50', '#2196F3']
    _, ax1 = plt.subplots()
    ax1.pie(values, colors=colors, startangle=90, counterclock=False, autopct='%1.1f%%', pctdistance=0.85,
            labeldistance=1.05)
    ax1.axis('equal')
    ax1.set_title("Emission Categories")
    ax1.legend(categories, loc="best")
    plt.show()

def calculate_clothing_carbon_footprint(num_items, materials) -> float:
    """Calculate the carbon footprint of clothing based on the materials used.

    Arguments:
    num_items -- number of items
    materials -- list of materials the user has

    Returns:
    the carbon footprint per clothing item
    """
    carbon_footprint = 0
    for material in materials:
        if material == "cotton":
            carbon_footprint += 5
        elif material == "polyester":
            carbon_footprint += 2
        elif material == "nylon":
            carbon_footprint += 7
    per_item_footprint = carbon_footprint / num_items
    return per_item_footprint

def suggest_actions(per_item_footprint) -> None:
    """Suggest actions to reduce the per-item carbon footprint of clothing.

    Arguments:
    per_item_footprint -- the carbon footprint per clothing item
    """
    if per_item_footprint > 5:
        print("Your clothing carbon footprint is high. Consider making these changes:")
        print("- Choose clothes made from sustainable materials such as organic cotton, bamboo, or hemp")
        print("- Shop at thrift stores or clothing rental services to reduce waste")
        print("- Avoid fast fashion brands that produce large amounts of low-quality clothing")
    elif per_item_footprint > 3:
        print("Your clothing carbon footprint is moderate. Consider making these changes:")
        print("- Wash clothes in cold water and hang dry instead of using the dryer")
        print("- Donate or recycle old clothing instead of throwing it away")
        print("- Choose high-quality clothes that last longer")
    else:
        print("Your clothing carbon footprint is low. Keep up the good work!")

def main1():
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

def main2():
    materials = []

    while True:
        try:
            number_of_materials = int(input("Approximately how many pieces of clothing do you own?\n"))
            break
        except ValueError:
            print("\033[31mPlease answer with an integer\033[0m")

    while True:
        cotton = str(input("do you own any cotton clothes? (Y/N)\n"))
        if cotton.lower() == "y" or cotton.lower() == "n":
            if cotton.lower() == "y":
                materials.append("cotton")
            break
        else:
            print("\033[31mPlease answer with Y/N\033[0m")

    while True:
        polyester = str(input("do you own any polyester clothes? (Y/N)\n"))
        if polyester.lower() == "y" or polyester.lower() == "n":
            if polyester.lower() == "y":
                materials.append("polyester")
            break
        else:
            print("\033[31mPlease answer with Y/N\033[0m")

    while True:
        nylon = str(input("do you own any nylon clothes? (Y/N)\n"))
        if nylon.lower() == "y" or nylon.lower() == "n":
            if nylon.lower() == "y":
                materials.append("nylon")
            break
        else:
            print("\033[31mPlease answer with Y/N\033[0m")

    per_item_footprint = calculate_clothing_carbon_footprint(number_of_materials, materials)
    suggest_actions(per_item_footprint)

if __name__ == '__main__':

    while True:
        choice = input("-Choose a to calculate your emission\n-Choose b to calculate your clothing emission ")
        if choice == "a" or choice == "b":
            break
        else:
            print("\033[31mPlease answer with a or b\033[0m")

    if choice == "a":
        main1()
    else:
        main2()
