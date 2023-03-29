import csv
import os

# function to calculate monthly electrical usage
def calc_monthly_usage(devices):
    total_usage = sum([float(device[1]) for device in devices])
    monthly_usage = total_usage * 30  # assuming 30 days in a month
    return monthly_usage

# get path to CSV file in same directory as script
script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, "household_devices.csv")

# read CSV file and store data in a list
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    devices = [row for row in reader]

# calculate monthly electrical usage
monthly_usage = calc_monthly_usage(devices)

# display message based on electrical usage
if monthly_usage > 300:
    print("Your household has a high monthly electrical usage. Consider reducing usage to help the environment.")
else:
    print("Your household has a reasonable monthly electrical usage. Keep up the good work!")
