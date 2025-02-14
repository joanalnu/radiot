# script to read the nuclid parameters from nist-nuclide-data.txt a dataset by the NIST institute
import os
from library import lib

# Define the path to the input file
dirpath = os.path.dirname(__file__)
input_file_path = os.path.join(dirpath, '../nist-nuclide-data.txt')

# Initialize an empty list to store nuclide data
nuclide_data = []

# Read the input file
with open(input_file_path, 'r') as f:
    lines = f.readlines()

# Process the lines to extract nuclide information
nuclide_info = {}
for line in lines:
    line = line.strip()
    if line.startswith("Atomic Number"):
        if nuclide_info:  # If there's already data, save it before starting a new one
            nuclide_data.append(tuple(nuclide_info.values()))
            nuclide_info = {}  # Reset for next nuclide

    # Extract key-value pairs from each line
    if '=' in line:
        key, value = line.split('=', 1)
        key = key.strip().lower().replace(' ', '_')  # Normalize key
        value = value.strip().replace('(', '').replace(')', '')  # Clean value
        nuclide_info[key] = value

# Don't forget to add the last nuclide after exiting the loop
if nuclide_info:
    nuclide_data.append(tuple(nuclide_info.values()))

# Write the data into library.py
with open('./library.py', 'w') as f:
    f.write("lib = {\n")
    f.write("    ('atomic_number', 'atomic_symbol', 'mass_number', 'relative_atomic_mass', 'isotopic_composition', 'standard_atomic_weight', 'notes'),\n")
    for entry in nuclide_data:
        f.write(f"    {entry},\n")
    f.write("}\n")

print("Nuclide data has been written to library.py successfully.")
