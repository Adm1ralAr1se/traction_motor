import pandas as pd
import matplotlib.pyplot as plt
from config import file_path

def import_excel_data(file_path):
    """
    Function to import data from an Excel file.
    
    Parameters:
    file_path (str): The path to the Excel file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the data from the Excel file.
    """
    # Read the Excel file using pandas
    data = pd.read_excel(file_path)
    return data

# Import data from the specified file path
data = import_excel_data(file_path)

# Print the entire DataFrame to the console
print(data)

# Display the first few rows of the DataFrame
data.head()

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

# Plot data
plt.plot(data['MPH'], data['INDEX_TR1'])
plt.plot(data['MPH'], data['INDEX_TR2'])
plt.plot(data['MPH'], data['INDEX_TR3'])
plt.plot(data['MPH'], data['INDEX_TR4'])
plt.xlabel('MPH')
plt.ylabel('Traction Index')
plt.legend(['INDEX_TR1', 'INDEX_TR2', 'INDEX_TR3', 'INDEX_TR4'])
plt.show()