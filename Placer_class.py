''' This module defines a placer class that is designed based on simulated
annealing optimization of a half-parameter bounding box cost function.'''
import random as RND
from numpy import exp, std, mean,log, absolute, floor

class sa_placer_agent():
    def __init__(self, chip_obj, max_iterations, verbose=0):
        self.verbose = verbose
        self.temp_schedule = []
        self.max_iter = max_iterations
        self.T = 0
        self.num_iter = 0
        self.chip = chip_obj
        self.current_delta_cost = 0
        self.sigma=0
        self.max_param_sample = 10000
        self.no_change = 0
        self.accepted = True
        self.num_rejection = 0
        self.num_acceptance = 0
        self.epsilon = 0.0001

    def param_initialization(self):
        '''
        The initialization is based on improvements suggested by:
        VLSI cell placement Techniques
        K shahkoor and P. mazumder
        '''
        self.Kai0 = .90

        DELTA_C=[]
        DELTA_C_PLUS = []

        m2=0
        m1=0

        for i in range(self.max_param_sample):
            cell_i, cell_j, delta_cost = self.random_swap()
            DELTA_C.append(delta_cost)

            if delta_cost > 0:
                DELTA_C_PLUS.append(delta_cost)
                m2 += 1
            elif delta_cost <=0:
                m1 += 1

        self.sigma = std(DELTA_C)


        DELTA_C_PLUS_AVG = mean(DELTA_C_PLUS)

        self.T = DELTA_C_PLUS_AVG/ \
        (log(m2*1.0/(m2*self.Kai0  - (1-self.Kai0 )*m1)))


        print '-'*50
        print 'SA INITIALIZATION'
        print "mean DC+" , DELTA_C_PLUS_AVG
        print "sigma", self.sigma
        print 'm1', m1
        print 'm2', m2
        print 'temp' , self.T
        print '-'*50

    def update_temperature(self):
        ''' Temperature update based on Huang et al. [1986]
        '''
        self.T = self.T * exp(self.T * self.current_delta_cost/self.sigma**2)

    def random_swap(self):

        [i,j] = RND.sample(range(self.chip.num_cells),2)

        delta_cost = self.chip.swap_delta_cost(i,j)

        return i,j, delta_cost

    def make_move(self):

        cell_i, cell_j, delta_cost = self.random_swap()

        if RND.uniform(0, 1) <= exp(-delta_cost/self.T):
            self.chip.commit_swap_cells(cell_i,cell_j)
            self.current_delta_cost = delta_cost
            self.accepted = True
        else:
            self.accepted = False
        self.update_temperature()

    def anneal(self):
        self.param_initialization()

        while (self.num_iter <= self.max_iter) and \
         (self.no_change <= 0.1 * self.max_iter):


            self.make_move()

            # Book keeping section for SA:
            self.num_iter += 1

            if self.accepted == False:
                self.num_rejection += 1
            else:
                self.num_acceptance += 1

            if absolute(self.current_delta_cost) < self.epsilon:
                self.no_change += 1
            else:
                self.no_change = 0

            # Printing every 1% of the whole process ...
            if self.num_iter % int(floor(0.01 * self.max_iter)) == 0:
                print '>>> Temp:', self.T,', Iter:', self.num_iter,\
                ', Cost:' , self.chip.total_cost
