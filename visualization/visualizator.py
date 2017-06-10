import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Visualizator:
    def __init__(self):
        pass

    @staticmethod
    def plot_state(problem, state, label):
        fig = plt.figure(figsize=(40, 40))
        ax = fig.add_subplot(121, aspect='equal')
        # draw boxes
        for box in problem.boxes:
            vertex = box.vertices['bo_lf']
            patch = patches.Rectangle((vertex.x, vertex.y), box.width, box.height, fill=False)
            ax.add_patch(patch)
            # draw check points
            x_coords = []
            y_coords = []
            colors = []
            for point in box.checkpoints:
                x_coords.append(point.x)
                y_coords.append(point.y)
                colors.append('g' if point.is_observed else 'r')
            plt.scatter(x_coords, y_coords, s=10, c=colors)
        # draw cameras
        for camera in state.cameras:
            circle = plt.Circle((camera.pos.x, camera.pos.y), problem.camera_range, color='b', fill=False)
            ax.add_artist(circle)
        # save figure
        fig.savefig(label + '.png', dpi=180, bbox_inches='tight')

    @staticmethod
    def plot_values_results(values_results, param, tested):
        # coords arrays
        x_points = []
        y_points = []
        x = []
        y_means = []
        y_std_devs = []
        # plot figure
        fig = plt.figure(figsize=(10, 10))
        # for every key in values results dict
        for value in sorted(values_results):
            # compute mean and standard deviation
            n_results = len(values_results[value])
            mean = 0 if n_results == 0 else sum(values_results[value]) / n_results
            diff = [(result - mean)**2 for result in values_results[value]]
            std_dev = 0 if n_results == 0 else (sum(diff) / n_results)**.5
            # save computed values
            x.append(value)
            y_means.append(mean)
            y_std_devs.append(std_dev)
            # save point coords
            for result in values_results[value]:
                x_points.append(value)
                y_points.append(result)
            # draw points, mean and std deviation
            plt.scatter(x_points, y_points, s=[20]*len(x_points), c=['orange']*len(x_points))
            plt.errorbar(x, y_means, xerr=0, yerr=y_std_devs, marker="o", color='red', ecolor='blue', markersize='3', capsize=10,
                     elinewidth=1)
        # save figure
        fig.savefig(param + '_test_on_' + tested + '.png', dpi=90)

    @staticmethod
    def plot_costs(costs):
        # plot figure
        fig = plt.figure(figsize=(10, 10))
        # draw line
        plt.plot(range(len(costs)), costs)
        # save figure
        fig.savefig('costs.png', dpi=90)
