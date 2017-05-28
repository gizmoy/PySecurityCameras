from domain import state
from visualization import visualizator


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.log = []
        self.problem = problem
        self.temperature = config['temperature']
        self.max_iterations = config['max_iterations']
        self.generate_initial_state()

    def generate_initial_state(self):
        st = state.State(self.problem)
        st.generate_cameras(self.problem.boxes, self.problem.max_cameras)
        self.log.append(st)

    def perform(self):
        # get last state from log and init values
        x = self.log[-1]
        iteration = 1

        visualizator.Visualizator.plot(self.problem, x, 0)
        # perform simulated annealing
        while iteration < self.max_iterations:
            print 'iteration %d and only %d to go' % (iteration, self.max_iterations - iteration)
            y = x.generate_neighbour()
            visualizator.Visualizator.plot(self.problem, y, iteration)
            x = y
            iteration += 1


