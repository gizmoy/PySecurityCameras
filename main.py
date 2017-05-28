import json
from optparse import OptionParser

from metaheuristics.simulated_annealing import simulated_annealing
from visualization import visualizator
from domain import problem


if __name__ == '__main__':
    # create parser & parse args
    parser = OptionParser()
    parser.add_option('-f', '--file', action='store', dest='filename', default='config.json',
                      help='File with problem configuration')
    (options, args) = parser.parse_args()

    # check if name of file is a json one
    filename = options.filename
    if not filename.endswith('.json'):
        raise ValueError('A configuration file must be a json one!')

    # read config from file
    with open(filename) as config_file:
        config = json.load(config_file)

    # define problem and perform algorithm
    problem = problem.Problem(config)
    algorithm = simulated_annealing.SimulatedAnnealing(config, problem)
    algorithm.perform()