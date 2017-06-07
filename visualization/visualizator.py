import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Visualizator:
    def __init__(self):
        pass

    @staticmethod
    def plot(problem, state, iteration=None, label=None):
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
        fig.savefig('state_of_' + str(iteration) + '_' + label + '.png', dpi=180, bbox_inches='tight')