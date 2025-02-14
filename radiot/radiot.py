import numpy as np
import matplotlib.pyplot as plt


class DecayChain:
    def __init__(self, nuclide_data):
        """
        Initialize the DecayChain class with nuclide data.

        :param nuclide_data: List of tuples containing nuclide information.
        """
        self.nuclide_data = nuclide_data  # Store the nuclide data
        self.decay_chain = []  # To store the decay chain
        self.final_amounts = {}  # To store final amounts of each nuclide

    def find_decay_chain(self, starting_nuclide):
        """
        Find the decay chain starting from a given nuclide.

        :param starting_nuclide: The atomic symbol or name of the starting nuclide.
        """
        # Logic to find the decay chain based on starting_nuclide
        pass

    def chain_chart(self):
        """
        Make a flow chart of the decay chain starting from a given nuclide, or using an already chain list (outputed by find_decay_chain).

        :param decay_chain: The decay chain outputed by find_decay_chain.
        :return: show and save figure (png)
        """

    def compute_decay_time(self, nuclide):
        """
        Compute the decay time (half-life) for a given nuclide.

        :param nuclide: The nuclide for which to compute the decay time.
        :return: Half-life of the nuclide.
        """
        # Logic to compute half-life from nuclide data
        pass

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
