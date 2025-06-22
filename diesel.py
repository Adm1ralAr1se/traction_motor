import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import file_path_diesel

def import_excel_data(file_path_diesel):
    """
    Function to import data from an Excel file.
    
    Parameters:
    file_path (str): The path to the Excel file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the data from the Excel file.
    """
    # Read the Excel file using pandas
    data = pd.read_excel(file_path_diesel)
    return data

# Import data from the specified file path
data = import_excel_data(file_path_diesel)

# Print the entire DataFrame to the console
print(data)

# Display the first few rows of the DataFrame
data.head()

# Calculate standard deviation and average for each MPH value across the traction indices
data['STD_DEV'] = data[['TR1', 'TR2', 'TR3', 'TR4']].std(axis=1, ddof=0)
data['AVG'] = data[['TR1', 'TR2', 'TR3', 'TR4']].mean(axis=1)

# Print the standard deviation and average for each MPH value
for index, row in data.iterrows():
    print(f"MPH: {row['MPH']}, Standard Deviation: {row['STD_DEV']}, Average: {row['AVG']}")

# Calculate the absolute differences (deltas) between the traction indices
# for different pairs of indices
delta_1_2 = abs(data['INDEX_TR1'] - data['INDEX_TR2'])
delta_1_3 = abs(data['INDEX_TR1'] - data['INDEX_TR3'])
delta_1_4 = abs(data['INDEX_TR1'] - data['INDEX_TR4'])
delta_2_3 = abs(data['INDEX_TR2'] - data['INDEX_TR3'])
delta_2_4 = abs(data['INDEX_TR2'] - data['INDEX_TR4'])
delta_3_4 = abs(data['INDEX_TR3'] - data['INDEX_TR4'])

# Find the maximum delta for each pair of indices
maxdelta_1_2 = delta_1_2.max()
max_delta_1_3 = delta_1_3.max()
max_delta_1_4 = delta_1_4.max()
max_delta_2_3 = delta_2_3.max()
max_delta_2_4 = delta_2_4.max()
max_delta_3_4 = delta_3_4.max()

# Determine the overall maximum delta from all pairs
max_delta = max(maxdelta_1_2, max_delta_1_3, max_delta_1_4, max_delta_2_3, max_delta_2_4, max_delta_3_4)

# Find the corresponding MPH (Miles Per Hour) value for the maximum delta
if max_delta == maxdelta_1_2:
    # If the maximum delta is from the pair INDEX_TR1 and INDEX_TR2
    mph_at_max_delta = data['MPH'][delta_1_2.idxmax()]
elif max_delta == max_delta_1_3:
    # If the maximum delta is from the pair INDEX_TR1 and INDEX_TR3
    mph_at_max_delta = data['MPH'][delta_1_3.idxmax()]
elif max_delta == max_delta_1_4:
    # If the maximum delta is from the pair INDEX_TR1 and INDEX_TR4
    mph_at_max_delta = data['MPH'][delta_1_4.idxmax()]
elif max_delta == max_delta_2_3:
    # If the maximum delta is from the pair INDEX_TR2 and INDEX_TR3
    mph_at_max_delta = data['MPH'][delta_2_3.idxmax()]
elif max_delta == max_delta_2_4:
    # If the maximum delta is from the pair INDEX_TR2 and INDEX_TR4
    mph_at_max_delta = data['MPH'][delta_2_4.idxmax()]
else:
    # If the maximum delta is from the pair INDEX_TR3 and INDEX_TR4
    mph_at_max_delta = data['MPH'][delta_3_4.idxmax()]

# Print the maximum delta and the corresponding MPH value
print(f"The maximum delta is {max_delta} and it occurs at {mph_at_max_delta} MPH.")

# Calculate the maximum delta for each MPH
data['MAX_DELTA'] = pd.concat([delta_1_2, delta_1_3, delta_1_4, delta_2_3, delta_2_4, delta_3_4], axis=1).max(axis=1)
# # Plot data
# plt.plot(data['MPH'], data['INDEX_TR1'])
# plt.plot(data['MPH'], data['INDEX_TR2'])
# plt.plot(data['MPH'], data['INDEX_TR3'])
# plt.plot(data['MPH'], data['INDEX_TR4'])
# plt.xlabel('MPH')
# plt.ylabel('Traction Index')
# plt.legend(['INDEX_TR1', 'INDEX_TR2', 'INDEX_TR3', 'INDEX_TR4'])
# plt.show()

# # Plot the standard deviation in a separate line graph
# plt.figure(figsize=(8, 6))  # Create a new figure with a specific size
# plt.plot(data['MPH'], data['STD_DEV'], label='Standard Deviation', color='blue', linestyle='-', marker='o')

# # Add labels, title, and legend
# plt.xlabel('MPH')
# plt.ylabel('Standard Deviation')
# plt.title('Standard Deviation of Traction Indices vs MPH')
# plt.legend()

# # Show the plot
# plt.grid(True)  # Add grid for better readability
# plt.show()




# # Plot the maximum delta in a separate line graph
# plt.figure(figsize=(10, 6))  # Create a new figure with a specific size
# plt.plot(data['MPH'], data['MAX_DELTA'], label='Maximum Delta', color='red', linestyle='-', marker='o')

# # Add labels, title, and legend
# plt.xlabel('MPH')
# plt.ylabel('Delta Values')
# plt.title('Maximum Delta vs MPH')
# plt.legend()

# # Show the plot
# plt.grid(True)  # Add grid for better readability
# plt.show()

# Set figure size for a 3.5 inch screen and adjust font/marker sizes
fig, axes = plt.subplots(2, 2, figsize=(3.5, 2.5), gridspec_kw={'height_ratios': [1, 0.5], 'hspace': 0.4, 'wspace': 0.3})

# Plot traction indices in the first subplot
axes[0, 0].plot(data['MPH'], data['INDEX_TR1'], label='INDEX_TR1', linestyle='-', marker='o', markersize=3, linewidth=1)
axes[0, 0].plot(data['MPH'], data['INDEX_TR2'], label='INDEX_TR2', linestyle='-', marker='s', markersize=3, linewidth=1)
axes[0, 0].plot(data['MPH'], data['INDEX_TR3'], label='INDEX_TR3', linestyle='-', marker='^', markersize=3, linewidth=1)
axes[0, 0].plot(data['MPH'], data['INDEX_TR4'], label='INDEX_TR4', linestyle='-', marker='v', markersize=3, linewidth=1)
axes[0, 0].set_title('Traction Indices vs MPH', fontsize=7)
axes[0, 0].set_xlabel('MPH', fontsize=6)
axes[0, 0].set_ylabel('Traction Index', fontsize=6)
axes[0, 0].legend(fontsize=5)
axes[0, 0].grid(True, linewidth=0.3)

# Plot standard deviation in the second subplot
axes[0, 1].plot(data['MPH'], data['STD_DEV'], label='Standard Deviation', color='blue', linestyle='-', marker='o', markersize=3, linewidth=1)
axes[0, 1].set_title('Std Dev of Traction Indices vs MPH', fontsize=7)
axes[0, 1].set_xlabel('MPH', fontsize=6)
axes[0, 1].set_ylabel('Std Dev', fontsize=6)
axes[0, 1].legend(fontsize=5)
axes[0, 1].grid(True, linewidth=0.3)

# Remove the bottom-right subplot created by plt.subplots
fig.delaxes(axes[1, 0])  # Deletes the bottom-left subplot
fig.delaxes(axes[1, 1])  # Deletes the bottom-right subplot


# Plot maximum delta in the third subplot
ax_bottom = fig.add_subplot(2, 1, 2)  # Add a subplot that spans the entire bottom row
ax_bottom.plot(data['MPH'], data['MAX_DELTA'], label='Maximum Delta', color='red', linestyle='-', marker='o', markersize=3, linewidth=1)
ax_bottom.fill_between(data['MPH'], data['MAX_DELTA'], color='red', alpha=0.2, label='Shaded Region')
ax_bottom.set_title('Max Delta vs MPH', fontsize=7)
ax_bottom.set_xlabel('MPH', fontsize=6)
ax_bottom.set_ylabel('Max Delta', fontsize=6)
ax_bottom.legend(fontsize=5)
ax_bottom.grid(True, linewidth=0.3)

# Adjust layout to prevent overlap
plt.tight_layout(pad=1.0) # Add padding between subplots
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15, hspace=0.5, wspace=0.2)

# Show the figure
plt.show()