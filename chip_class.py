''' This module defines a chip object that contains information about its cells,
The size of the chip, the net lists and position of each cell on the chip.'''
import random as random
from numpy import floor

class chip():
    def __init__(self, rows, cols, cells, conns, net_list):

        # initialize object constants:
        self.num_rows = rows
        self.num_cols = cols
        self.num_cells = cells
        self.num_nets = conns
        self.net_list = net_list

        # initialize object variables:
        self.area = self.num_rows * self.num_cols

        self.cell_location={}
        self.reset_cell_location()

        # Calculate the current total cost:
        self.cost_half_param()

    def reset_cell_location(self):

        # Empty the current location dict:
        self.cell_location={}

        # create random locations:
        indices = random.sample(xrange(self.area), self.num_cells)
        random_locations =  list(range(self.area)[i] for i in indices)

        print random_locations

        # resent all locations to their random locations:
        for i in range(self.num_cells):
            y = int(floor(random_locations[i]*1.0 / self.num_cols))
            x = int(random_locations[i] - y * self.num_cols)
            self.cell_location[i] = (x,y)

    def calculate_bounding_box(self, net_ID):
        rows = []
        cols = []
        for cell in self.net_list[net_ID]:
            cols.append(self.cell_location[cell][0])
            rows.append(self.cell_location[cell][1])

        delta_y = max(rows) - min(rows)
        delta_x = max(cols) - min(cols)

        return delta_x + delta_y

    def cost_half_param(self):

        self.total_cost=0

        for net in range(self.num_nets):
            self.total_cost += self.calculate_bounding_box(net)

    def display(self):
        print 'Current Cell locations:'
        print self.cell_location

        print 'The current cost:'
        print self.total_cost
