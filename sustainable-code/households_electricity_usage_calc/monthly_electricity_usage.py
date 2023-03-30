import csv
import os
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Get path of script and CSV file in same directory
script_path = os.path.abspath(__file__)
csv_path = os.path.join(os.path.dirname(script_path), 'household_devices.csv')

# Load data from CSV
data = []
with open(csv_path) as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        data.append(row)

# Calculate monthly usage
total_usage = 0
for device in data:
    total_usage += float(device[1])
monthly_usage = total_usage * 30  # Assuming 30 days in a month

# Sort devices by usage
data_sorted = sorted(data, key=lambda x: float(x[1]), reverse=True)

# Plot bar chart
fig = Figure(figsize=(8, 6))

bar_width = 0.5
opacity = 0.8
index = [i * bar_width for i in range(len(data_sorted))]

bars = fig.add_subplot(111).bar(index, [float(device[1]) for device in data_sorted], bar_width,
              alpha=opacity, color='b', edgecolor='k')

fig.axes[0].set_xticks(index)
fig.axes[0].set_xticklabels([device[0] for device in data_sorted], rotation='vertical', fontsize=7)

fig.axes[0].set_xlabel('Devices')
fig.axes[0].set_ylabel('Electric usage (kW)')

# Set y-axis limit slightly above maximum value to prevent clipping of tallest bar
fig.axes[0].set_ylim(0, max([float(device[1]) for device in data_sorted]) * 1.1)

# Add spacing between bars
fig.tight_layout(pad=1)

# Create Tkinter GUI
root = tk.Tk()
root.title('Electric Usage')

# Create canvas for plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add scrollbar
scrollbar = tk.Scrollbar(master=root, orient=tk.VERTICAL, command=canvas.get_tk_widget().yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.get_tk_widget().configure(yscrollcommand=scrollbar.set)

# Bind mouse scroll to scrollbar
def _on_mousewheel(event):
    canvas.get_tk_widget().yview_scroll(int(-1*(event.delta/120)), "units")
canvas.get_tk_widget().bind_all("<MouseWheel>", _on_mousewheel)

root.mainloop()
