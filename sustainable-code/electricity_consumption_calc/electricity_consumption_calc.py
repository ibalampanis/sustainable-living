import csv
import os
import tkinter as tk
from tkinter import ttk

# Get path of script and CSV file in same directory
script_path = os.path.abspath(__file__)
csv_path = os.path.join(os.path.dirname(script_path), 'devices.csv')

# Open the CSV file and extract each device name and power consumption from the first two columns
device_info = []
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        device_info.append((row[0], float(row[1]), float(row[2])))

# Initialize the GUI
root = tk.Tk()
root.title('Device Selector')

# Define a custom style for the Checkbuttons
style = ttk.Style()
style.configure('Custom.TCheckbutton', background=root.cget('bg'), foreground='black')

# Create Checkbutton widgets for each device name
buttons = []
columns = 7
rows = (len(device_info) + columns - 1) // columns
for i in range(rows):
    frame = tk.Frame(root)
    frame.pack(side='top', fill='x')
    for j in range(columns):
        index = i * columns + j
        if index < len(device_info):
            var = tk.BooleanVar(value=False)
            button = ttk.Checkbutton(frame, text=device_info[index][0], variable=var, style='Custom.TCheckbutton')
            button.pack(side='left', padx=5, pady=5)
            buttons.append((var, device_info[index]))


# Define a function to handle button presses
# Define a function to handle button presses
def on_button_press():
    selected_devices = [name for var, (name, _, _) in buttons if var.get()]
    total_consumption = sum(hours * power / 1000 for name, power, hours in device_info if name in selected_devices)
    monthly_consumption = total_consumption * 30  # Assuming 30 days in a month

    message = ""
    if monthly_consumption < 100:
        message = "Your monthly energy consumption is very good!"
    elif monthly_consumption < 200:
        message = "Your monthly energy consumption is good."
    elif monthly_consumption < 300:
        message = "Your monthly energy consumption is okay, but you could do better."
    elif monthly_consumption < 400:
        message = "Your monthly energy consumption is bad. You should consider reducing the number of devices you use."
    else:
        message = "Your monthly energy consumption is very bad. Please reduce the number of devices you use for the sake of the environment."

    results_label.config(
        text=f"Selected devices: {', '.join(selected_devices)}\nTotal energy consumption: {total_consumption:.2f} kWh\nMonthly energy consumption: {monthly_consumption:.2f} kWh\n\n{message}")


# Add a button to submit the selection
submit_button = tk.Button(root, text='Calculate', command=on_button_press)
submit_button.pack(pady=10)

# Add a label to show the results
results_label = tk.Label(root, text="")
results_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
