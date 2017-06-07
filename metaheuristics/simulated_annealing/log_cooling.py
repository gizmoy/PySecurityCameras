import math


class LogCooler:
    def __init__(self, config):
        self.tau = config['cooling']['tau']
        self.iteration = 0

    def get_temperature(self):
        temperature = self.tau / (1 + math.log(1 + self.iteration))
        self.iteration += 1
        return temperature
