import matplotlib.pyplot as plt
from graphviz import Digraph

from symbols import atomic_symbols, atomic_numbers
from library import lib
from pyne import data as nd
import math


# the activity R at time t can be calculated using the equation: $R = R_0 ^{-\lambda t}$
# the number of radiactive nuclei remaining after time t is: $N = N_0 e^{-\lambda t}$



class DecayChain:
    def __init__(self):
        """
        Initialize the DecayChain class with nuclide data.

        :param nuclide_data: List of tuples containing nuclide information.
        """
        self.nuclide_data = lib  # Store the nuclide data
        self.decay_chain = []  # To store the decay chain
        self.final_amounts = {}  # To store final amounts of each nuclide

    def get_nuclide_data(self, starting_nuclide):
        """
        Access the data for a specific nuclide based on mass number and atomic symbol.

        :param starting_nuclide: a tuple consisting of (mass_number, atomic_symbol)
        :return: the corresponding list or None if not found.
        """
        mass_number, atomic_symbol = starting_nuclide
        for nuclide in self.nuclide_data:
            if nuclide[2] == mass_number and nuclide[1] == atomic_symbol:
                return nuclide

        return None

    def atomicsymbol_2_atomicnumber(self, atomic_symbol):
        """
        :param atomic_symbol: string containing atomic symbol
        :return: atomic_number: integer representing the atomic number of the given symbol
        """
        return atomic_numbers[atomic_symbol]

    def atomicnumber_2_atomicsymbol(self, atomic_number):
        """
        :param atomic_number: integer representing the atomic number
        :return: atmoic_symbol: string representing the atomic symbol of the given number
        """
        return atomic_symbols[atomic_number]

    def find_decay_chain(self, starting_nuclide):
        """
        Find the decay chain starting from a given nuclide.

        :param starting_nuclide: A tuple containing: (mass_number, atomic_number) or (mass_number, atomic_symbol)
        :return: A list representing the decay chain.
        """
        # Check if the second element is an integer (atomic number) or convert from atomic symbol
        if isinstance(starting_nuclide[1], int):
            current_nuclide = (int(starting_nuclide[0]), starting_nuclide[1])
        else:
            current_nuclide = (int(starting_nuclide[0]), self.atomicsymbol_2_atomicnumber(starting_nuclide[1]))

        dc = [current_nuclide]

        while True:
            nuclide_data = self.get_nuclide_data(current_nuclide)

            # Check for decay modes
            if 'a' in nuclide_data[6]:
                current_nuclide = (current_nuclide[0] - 4, current_nuclide[1] - 2)  # Alpha decay
                dc.append(('a', current_nuclide))
            elif 'b' in nuclide_data[6]:
                current_nuclide = (current_nuclide[0], current_nuclide[1] + 1)  # Beta decay
                dc.append(('b', current_nuclide))
            elif ('g' in nuclide_data[6] and 'a' not in nuclide_data[6]) or ('g' in nuclide_data[6] and 'b' not in nuclide_data[6]):
                dc.append(('g', 'g'))
                break
            else:
                break

        self.decay_chain = dc
        return dc  # Return the decay chain for further use

    from graphviz import Digraph  # Ensure you have this import at the top of your file

    def chain_chart(self):
        """
        Make a flow chart of the decay chain starting from a given nuclide,
        or using an already created chain list (outputted by find_decay_chain).

        :return: Show and save figure (PNG).
        """
        cmap = {
            'a': 'yellow',
            'b': 'blue'
        }

        if not self.decay_chain:
            raise ValueError("You must first run the find_decay_chain function to create a decay chain.")

        dc = self.decay_chain

        # Create directed graph
        dot = Digraph(f'{dc[0]}_decay_chain', format='png')
        dot.attr(rankdir='TB', size='12', dpi='600')
        dot.attr('node', shape='box', style='rounded, filled', color='lightblue', fontname='Arial', fontsize='12')

        for i in range(len(dc)):
            if isinstance(dc[i], tuple):
                radiation = dc[i][0]
                mass_number = dc[i][1][0]
                atomic_number = dc[i][1][1]
                node_id = f'{mass_number}_{atomic_number}'
                dot.node(node_id, f"{self.atomicnumber_2_atomicsymbol(atomic_number)}-{mass_number}", color=cmap[radiation])

                # Create edge from previous nuclide to current nuclide
                if i > 0 and isinstance(dc[i - 1], tuple): # only if previous nuclide existes!
                    prev_mass_number = dc[i - 1][1][0]
                    prev_atomic_number = dc[i - 1][1][1]
                    prev_id = f'{prev_mass_number}_{prev_atomic_number}'
                    dot.edge(prev_id, node_id, label=radiation)

            elif dc[i] == 'g':
                dot.node(f'gamma_{i}', 'Gamma Radiation', color='lightgrey')
                if i > 0 and isinstance(dc[i - 1], tuple):
                    prev_mass_number = dc[i - 1][1][0]
                    prev_atomic_number = dc[i - 1][1][1]
                    prev_id = f'{prev_mass_number}_{prev_atomic_number}'
                    dot.edge(prev_id, f'gamma_{i}', label='g')

        # Add a legend
        with dot.subgraph(name='legend') as legend:
            legend.attr(label='Legend', color='black', style='dashed')
            legend.node('a', 'Alpha Decay', color=cmap['a'])
            legend.node('b', 'Beta Decay', color=cmap['b'])

        # Save diagram
        dot.render(f"../{dc[0]}_decay_chain", cleanup=True)

        # Show diagram
        dot.view()  # This will open the generated PNG file

    def compute_decay_time(self):
        """
        Compute the total decay time for a given decay chain.

        This function calculates the total decay time of a decay chain
        by summing the half-lives of all the nuclides involved in the chain.

        :return: Total decay time for the chain.
        """
        dc = self.decay_chain
        total_decay_time = 0

        for item in dc:
            if isinstance(item, tuple) and len(item) == 2:
                decay_mode, (mass_number, atomic_number) = item
                try:
                    atomic_symbol = self.atomicnumber_2_atomicsymbol(atomic_number)
                    nuclide_name = f'{atomic_symbol}-{mass_number}'
                    decay_constant = nd.decay_const(nuclide_name)
                    half_life = math.log(2) / decay_constant
                    total_decay_time += half_life
                except KeyError as e:
                    print(f"Decay constant not found for {nuclide_name}: {e}")
                except Exception as e:
                    print(f"Error computing decay time for {nuclide_name}: {e}")

        return total_decay_time

    def simulate_decay(self, initial_amount, time_period): # time_period should be the sum of the half-times of the chain, unless a specific value is provided
        """
        Simulate the decay process over a specified time period.

        :param initial_amount: Initial amount of the starting nuclide.
        :param time_period: Total time over which to simulate decay.
        :return: A dictionary with final amounts of each transited element.
        """
        # Logic to simulate decay and calculate final amounts
        pass

    def calculate_percentages(self):
        """
        Calculate the percentages of each transited element left in the sample after decay.

        :return: A dictionary with percentages of each element.
        """
        # Logic to calculate percentages
        pass

    def plot_decay_results(self):
        """
        Plot a pie chart showing the percentages of each transited element remaining after decay.
        """
        percentages = self.calculate_percentages()

        # Create pie chart using matplotlib
        labels = percentages.keys()
        sizes = percentages.values()

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Decay Chain Results')
        plt.show()

# Example usage:
# Assuming you have loaded your nuclide data into a variable called `nuclide_data`
# decay_chain = DecayChain(nuclide_data)
# decay_chain.find_decay_chain('Starting_Nuclide_Symbol')
# decay_chain.simulate_decay(initial_amount=1000, time_period=5000)
# decay_chain.plot_decay_results()
