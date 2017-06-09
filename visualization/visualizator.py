import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Visualizator:
    def __init__(self):
        pass

    @staticmethod
    def plot(problem, state, label):
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
        fig = plt.figure(figsize=(20, 20))
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
                (_, caps, _) = plt.errorbar(x, y_means, xerr=0, yerr=y_std_devs)
                # set color and width of caps
                for cap in caps:
                    cap.set_color('red')
                    cap.set_markeredgewidth(5)
        # draw points
        plt.scatter(x_points, y_points, s=20)
        # save figure
        fig.savefig('test_of_' + tested + '_on_' + param + '.png', dpi=90)  #, bbox_inches='tight')

