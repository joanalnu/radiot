# create charts/plots of all nuclide

# 1. cmap of radioactive decay types
# 2. cmap of radioactive decay times 8when pyne is available
# 3. histogram of isotopes per atomic number

import matplotlib.pyplot as plt
from library import lib
import numpy as np

# 1
atomic_numbers = []
atomic_symbols = []
mass_numbers = []
decay_types = []
for nuclide in lib:
    atomic_numbers.append(nuclide[0])
    atomic_symbols.append(nuclide[1])
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

plt.figure()
plt.scatter(atomic_numbers, mass_numbers, color=cmap)
plt.xlabel(atomic_symbols)
plt.show()







# # 3
# atomic_numbers = np.linspace(1, 118, 118) # initialize indexes
#
# # create empty dictionary
# distribution_dict = {}
# for i in atomic_numbers:
#     distribution_dict[i] = 0
#
# # TODO: I think this could be done more efficiently, above all considering the dictionary is unuseful for plotting an histogram
# # count (iterating)
# for i in atomic_numbers:
#     for nuclide in lib:
#         if nuclide[0]==i:
#             distribution_dict[i] += 1
#
# plt.figure()