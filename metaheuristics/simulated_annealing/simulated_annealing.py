import random
import math
from domain.state import State
from metaheuristics.simulated_annealing.lin_cooling import LinCooler
from metaheuristics.simulated_annealing.exp_cooling import ExpCooler


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.problem = problem
        self.temperature = config['temperature']
        self.max_iterations = config['max_iterations']
        self.initial_state = State(self.problem)
        self.outcome = None
        # cooling
        cooling_type = config['cooling']['type']
        if cooling_type == 'lin':
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
        # perform simulated annealing
        while i < self.max_iterations:
            if i % 100 == 0:
                print 'iteration (%d/%d)' % (i, self.max_iterations)
            # generate y as neighbour of x and count their qualities
            y = x.generate_neighbour()
            x_cost = self.problem.get_state_loss(x, visualize=(i % 100 == 0), iteration=i)
            y_cost = self.problem.get_state_loss(y, visualize=(i % 101 == 0), iteration=i)
            # compute threshold and update x if y's cost < x's cost (minimisation) or random number < threshold
            threshold = math.exp(-math.fabs(y_cost - x_cost) / t) if t > 0 else 0
            if x_cost > y_cost or random.random() < threshold:
                print 'Zmieniam'
                x = y
            # update temperature and iteration counter
            t = self.cooler.get_temperature()
            i += 1
        # save outcome
        self.outcome = x

