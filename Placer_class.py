''' This module defines a placer class that is designed based on simulated
annealing optimization of a half-parameter bounding box cost function.'''
import random as RND
from numpy import exp

class sa_placer_agent():
    def __init__(self, chip_obj, initial_T, max_iterations):
        self.temp_schedule = []
        self.max_iter = max_iterations
        self.T = initial_T
        self.num_ietr = 0
        self.chip = chip_obj

    def random_swap(self):

        [i,j] = RND.sample(range(self.chip.num_cells),2)

        delta_cost = self.chip.swap_delta_cost(i,j)

        return i,j, delta_cost

    def make_move(self):

        cell_i, cell_j, delta_cost = self.random_swap()

        if delta_cost < 0 :
            self.chip.swap_cells(cell_i,cell_j)
            self.T = self.T*.95
        else:
            if RND.uniform(0, 1) <= exp(-delta_cost/self.T):
                self.chip.swap_cells(cell_i,cell_j)
                self.T = self.T*.95
            else:
                self.T = self.T*.95
    def anneal(self):

        while self.num_ietr <= self.max_iter:
            print 'iteration:', self.num_ietr,
            self.make_move()

            self.num_ietr += 1
            print 'done with cost' , self.chip.total_cost
