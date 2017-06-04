class LinCooler:
    def __init__(self, config):
        self.tau = config['cooling']['tau']
        self.base = config['cooling']['base']
        self.last_temperature = None

    def get_temperature(self):
        if self.last_temperature is None:
            self.last_temperature = self.tau
        else:
            self.last_temperature = self.last_temperature - self.base
        return self.last_temperature
