from domain import state
from visualization import visualizator


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.problem = problem
        self.temperature = config['temperature']
        self.max_iterations = config['max_iterations']
        self.initial_state = state.State(self.problem)

    def perform(self):
        # get last state from log and init values
        x = self.initial_state
        iteration = 1

        visualizator.Visualizator.plot(self.problem, x, 0)
        # perform simulated annealing
        while iteration < self.max_iterations:
            print 'iteration %d and only %d to go' % (iteration, self.max_iterations - iteration)
            y = x.generate_neighbour()
            visualizator.Visualizator.plot(self.problem, y, iteration)
            x = y
            iteration += 1


