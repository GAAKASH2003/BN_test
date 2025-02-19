import csv
import numpy as np
import os

file_paths = [
    'validation_data/set.000/coord.raw',
    'validation_data/set.000/energy.raw',
    'validation_data/set.000/force.raw',
    'validation_data/set.000/box.raw'
]
npy_directory = 'validation_data/set.000/'

for file_path in file_paths:
    try:
        # Initialize an empty list to store the arrays
        arrays = []

        with open(file_path, 'r') as file:
            for line in file:
                # Strip leading/trailing whitespace and split by spaces
                array = [float(x) for x in line.strip().split()]  # Convert to float
                arrays.append(array)

        # Ensure the file has data
        if not arrays:
            print(f"The file {file_path} is empty.")
            continue

        # Save to CSV
        csv_file = file_path.split('/')[-1].replace('.raw', '.csv')
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(arrays)
        print(f"Data successfully written to {csv_file}")

        # Convert CSV to NPY
        npy_file = os.path.join(npy_directory, os.path.basename(csv_file).replace('.csv', '.npy'))
        data = np.array(arrays)  # Already a NumPy array, no need to read CSV again
        np.save(npy_file, data)
        print(f"Data successfully saved to {npy_file}")

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
