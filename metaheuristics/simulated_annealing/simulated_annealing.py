import random
import math
import time
from domain.state import State
from metaheuristics.simulated_annealing.lin_cooling import LinCooler
from metaheuristics.simulated_annealing.exp_cooling import ExpCooler
from metaheuristics.simulated_annealing.log_cooling import LogCooler
from visualization.visualizator import Visualizator


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.problem = problem
        self.max_iterations = config['max_iterations']
        self.initial_state = State(self.problem)
        self.outcome = None
        self.outcome_cost = None
        self.exec_time = None
        # cooling
        cooling_type = config['cooling']['type']
        if cooling_type == 'log':
            self.cooler = LogCooler(config)
        elif cooling_type == 'lin':
            self.cooler = LinCooler(config)
        elif cooling_type == 'exp':
            self.cooler = ExpCooler(config)
        else:
            pass

    def perform(self):
        # get initial state and set initial values
        x = self.initial_state
        t = self.cooler.get_temperature()
        i = 0
        n_changes = 0
        costs = []
        start = time.time()
        # perform simulated
        x_cost = self.problem.get_state_cost(x, visualize=self.problem.verbose, label='init')
        costs.append(x_cost)
        while i < self.max_iterations:
            # print changes
            if self.problem.verbose == True and i % 100 == 0 and i != 0:
                print 'iteration (%d/%d) with %d changes and temperature %f & threshold %f' % (i, self.max_iterations, n_changes, t, threshold)
                n_changes = 0
            # generate y as neighbour of x and count their qualities
            y = x.generate_neighbour()
            y_cost = self.problem.get_state_cost(y)
            # compute threshold and update x if y's cost < x's cost (minimisation) or random number < threshold
            threshold = math.exp(-math.fabs((y_cost - x_cost)) / t) if t > 0 else 0
            if x_cost > y_cost or random.random() < threshold:
                n_changes += 1
                x, x_cost = y, y_cost
            # save x cost
            costs.append(x_cost)
            # update temperature and iteration counter
            t = self.cooler.get_temperature()
            i += 1
        # save outcome, cost and time
        self.outcome, self.outcome_cost = x, x_cost
        self.problem.get_state_cost(x, visualize=self.problem.verbose, label='outcome')
        self.exec_time = time.time() - start
        Visualizator.plot_costs(costs)

