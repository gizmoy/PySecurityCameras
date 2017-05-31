import random
import math
from domain import state


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.problem = problem
        self.temperature = config['temperature']
        self.max_iterations = config['max_iterations']
        self.initial_state = state.State(self.problem)
        self.outcome = None

    def perform(self):
        # get initial state and set initial values
        x = self.initial_state
        t = self.temperature
        iteration = 1
        # perform simulated annealing
        while iteration < self.max_iterations:
            print 'iteration %d and only %d to go' % (iteration, self.max_iterations - iteration)
            # generate y as neighbour of x and count their qualities
            y = x.generate_neighbour()
            x_cost = self.problem.get_state_cost(x)
            y_cost = self.problem.get_state_cost(y)
            print 'c_x: %f, c_y: %f' % (x_cost, y_cost)
            # compute threshold and update x if y's cost < x's cost (minimisation) or random number < threshold
            threshold = math.exp(-math.fabs(y_cost - x_cost) / t) if t > 0 else 0
            if x_cost > y_cost or random.random() < threshold:
                x = y
            print 'c_selected: %f' % x_cost
            # update iteration counter
            iteration += 1
        # save outcome
        self.outcome = x

