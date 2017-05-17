from domain import state


class SimulatedAnnealing:
    def __init__(self, config, problem):
        self.log = []
        self.problem = problem
        self.temperature = config['temperature']
        self.num_iterations = config['num_iterations']

    def generate_initial_state(self):
        st = state.State(self.problem)
        st.generate_cams(self.problem.boxes, self.problem.max_cameras)
        self.log.append(st)

    def perform(self):
        pass

