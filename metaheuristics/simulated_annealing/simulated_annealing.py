import random
import math
from domain.state import State
from metaheuristics.simulated_annealing.lin_cooling import LinCooler
from metaheuristics.simulated_annealing.exp_cooling import ExpCooler
from metaheuristics.simulated_annealing.log_cooling import LogCooler


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.problem = problem
        self.temperature = config['temperature']
        self.max_iterations = config['max_iterations']
        self.initial_state = State(self.problem)
        self.outcome = None
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
        # perform simulated
        x_cost = self.problem.get_state_loss(x, visualize=(i % 1000 == 0), iteration=i)
        while i < self.max_iterations:
            if i % 100 == 0:
                print 'iteration (%d/%d) and %d changes' % (i, self.max_iterations, n_changes)
                n_changes = 0
            # generate y as neighbour of x and count their qualities
            y = x.generate_neighbour()
            y_cost = self.problem.get_state_loss(y, visualize=(i % 1000 == 0), iteration=i)
            # compute threshold and update x if y's cost < x's cost (minimisation) or random number < threshold
            threshold = math.exp(-math.fabs(y_cost - x_cost) / t) if t > 0 else 0
            if x_cost > y_cost or random.random() < threshold:
                n_changes += 1
                x, x_cost = y, y_cost
            # update temperature and iteration counter
            t = self.cooler.get_temperature()
            i += 1
        # save outcome
        self.outcome = x
        self.problem.get_state_loss(x, visualize=True, iteration=-1)

