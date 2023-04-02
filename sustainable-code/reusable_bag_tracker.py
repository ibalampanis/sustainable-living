"""
This is a reusable bag calculator for tracking the number of reusable and disposable bags used,
and calculating the number of bags saved from landfill by using reusable bags.
"""


class ReusableBagTracker:
    """
    A reusable bag tracker that calculates the number of bags saved from landfill by using reusable bags.

    Attributes:
        total_reusable_bags (int): The total number of reusable bags used.
        total_disposable_bags (int): The total number of disposable bags used.

    Methods:
        add_bags(reusable_bags): Add the given number of reusable bags for each week in a year.
        add_disposable_bags(disposable_bags): Add the given number of disposable bags for each week in a year.
        get_savings(): Calculate the number of bags saved from landfill.

    """
    def __init__(self):
        self.total_reusable_bags = 0
        self.total_disposable_bags = 0

    def add_bags(self, reusable_bags):
        # Add the given number of reusable bags for each week in a year
        self.total_reusable_bags += reusable_bags

    def add_disposable_bags(self, disposable_bags):
        # Add the given number of disposable bags for each week in a year
        for i in range(52):
            self.total_disposable_bags += disposable_bags

    def get_savings(self):
        # Calculate the number of bags saved from landfill
        saved_bags = self.total_disposable_bags - self.total_reusable_bags
        return saved_bags


if __name__ == '__main__':
    tracker = ReusableBagTracker()

    while True:
        print("Enter the number of reusable bags used this year (or 'q' to quit):")
        reusable_input = input()
        if reusable_input == 'q':
            break
        try:
            reusable_bags = int(reusable_input)
            tracker.add_bags(reusable_bags)
            print("Enter the number of disposable bags you typically use every week:")
            disposable_bags = int(input())
            tracker.add_disposable_bags(disposable_bags)
            savings = tracker.get_savings()
            print("You saved", savings, "bags from landfill by using reusable bags!")
        except ValueError:
            print("Invalid input. Please enter a number of reusable bags or 'q' to quit.")
