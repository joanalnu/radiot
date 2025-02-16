
# create charts/plots of all nuclide

# 1. cmap of radioactive decay types
# 2. cmap of radioactive decay times 8when pyne is available
# 3. histogram of isotopes per atomic number

import matplotlib.pyplot as plt
from data.library import lib
import numpy as np
from data.symbols import atomic_symbols

# 1
atomic_numbers = []
atomic_symbols_lst = []
mass_numbers = []
decay_types = []
for nuclide in lib:
    atomic_numbers.append(nuclide[0])
    atomic_symbols_lst.append(nuclide[1])
    mass_numbers.append(nuclide[2])
    decay_types.append(nuclide[6])

cmap = []
for dt in decay_types:
    if 'a' in dt:
        cmap.append('yellow')
    elif 'b' in dt:
        cmap.append('blue')
    elif 'g' in dt:
        cmap.append('purple')
    elif 'm' in dt:
        cmap.append('pink')
    else:
        cmap.append('white')

# plt.figure()
# plt.scatter(atomic_numbers, mass_numbers, color=cmap)
# plt.xticks(range(1, 119, 5), atomic_symbols_lst, rotation=90)  # Adjusting tick labels every 5 elements
# plt.savefig('./nuclidechart.png', dpi=600)







# 3

atomic_numbers = np.linspace(1, 118, 118) # initialize indexes

# create empty dictionary
distribution_dict = {}

for i in atomic_numbers:
    distribution_dict[int(i)] = 0

# count (iterating)
for i in atomic_numbers:
    for nuclide in lib:
        if nuclide[0]==str(int(i)):
            distribution_dict[int(i)] += 1

plt.figure(figsize=(12,6))
plt.hist(distribution_dict.keys(), weights=distribution_dict.values(), bins=118, range=(1,118))
plt.xticks(range(1, 119, 5), [atomic_symbols[i] for i in range(1, 119, 5)], rotation=90)  # Adjusting tick labels every 5 elements
plt.xlabel("Atomic Number")
plt.ylabel("Number of Isotopes")
plt.show()
plt.savefig('./isotopes.png', dpi=600)
