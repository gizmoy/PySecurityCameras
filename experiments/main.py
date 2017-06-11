import json
import numpy as np
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
    interval_beg = experiment_config['interval']['beg']
    interval_end = experiment_config['interval']['end']
    num_values = experiment_config['num_values']
    num_tries = experiment_config['num_tries']
    param = experiment_config['param']
    tested = experiment_config['tested']

    # dictionary results of values: value(double) -> results(double[])
    values_results = {}

    for i in range(num_values):
        # sample value from the log space
        value = 10 ** np.random.uniform(interval_beg, interval_end)
        # change config value of examined parameter and init array of result for value
        config['cooling'][param] = value
        values_results[value] = []
        # verbose
        print 'Checking for %s == %f (value number %d out of %d)' % (param, value, i+1, num_values)
        # repeat algorithm n_tries times for one value
        for j in range(num_tries):
            # verbose
            print 'Try number %d out of %d' % (j+1, num_tries)
            # define problem and perform algorithm
            problem = Problem(config)
            algorithm = SimulatedAnnealing(config, problem)
            algorithm.perform()
            # saving one from: outcome state cost || len of cameras || number of unobserved points || execution time
            if tested == 'cost':
                result = algorithm.outcome_cost
            elif tested == 'num_cameras':
                result = len(algorithm.outcome.cameras)
            elif tested == 'unobserved_fraction':
                result = algorithm.outcome.num_unobserved / float(problem.num_checkpoints)
            elif tested == 'exec_time':
                result = algorithm.exec_time
            else:
                raise ValueError('Not recognized tested value name "%s"' % (tested))
            values_results[value].append(result)
    # plot values results
    Visualizator.plot_values_results(values_results, param, tested)
