import json
from optparse import OptionParser
from metaheuristics.simulated_annealing.simulated_annealing import SimulatedAnnealing
from domain.problem import Problem
from visualization.visualizator import Visualizator


if __name__ == '__main__':
    # create parser & parse args
    parser = OptionParser()
    parser.add_option('-F', '--file', action='store', dest='filename', default='experiment_config.json',
                      help='File with a configuration')
    (options, args) = parser.parse_args()

    # check if name of file is a json one
    filename = options.filename
    if not filename.endswith('.json'):
        raise ValueError('A configuration file must be a json one!')

    # read config from file
    with open(filename) as config_file:
        experiment_config = json.load(config_file)

    # problem configuration
    config = experiment_config['problem']

    # read experiment configuration
    values = experiment_config['values']
    n_tries = experiment_config['n_tries']
    param_name = experiment_config['param_name']

    # dictionary results of values: value(double) -> results(doubles[])
    values_results = {}

    for index, value in enumerate(values):
        # change config value of examined parameter
        config[param_name] = value
        # init array of results for value
        values_results[value] = []
        # verbose
        print 'Checking for %s == %f (value number %d out of %d)' % (param_name, value, index, len(values))
        for _ in range(n_tries):
            # define problem and perform algorithm
            problem = Problem(config)
            algorithm = SimulatedAnnealing(config, problem)
            algorithm.perform()
            # saving outcome state cost
            values_results[value].append(algorithm.outcome_cost)
    # plot results
    Visualizator.plot_values_results(values_results, param_name)
