import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Visualizator:
    def __init__(self):
        pass

    @staticmethod
    def plot(problem, state):
        fig = plt.figure(figsize=(40, 40))
        ax = fig.add_subplot(121, aspect='equal')
        # draw boxes
        for box in problem.boxes:
            vertex = box.get_vertex('bottom_left')
            patch = patches.Rectangle((vertex.x, vertex.y), box.width, box.height, fill=False)
            ax.add_patch(patch)
            # draw check points
            x_coords = []
            y_coords = []
            colors = []
            for check_point in box.check_points:
                x_coords.append(check_point.x)
                y_coords.append(check_point.y)
                colors.append('g' if check_point.is_observed else 'r')
            plt.scatter(x_coords, y_coords, s=10, c=colors)
        # draw cameras
        for camera in state.cameras:
            circle = plt.Circle((camera.pos.x, camera.pos.y), problem.camera_range, color='b', fill=False)
            ax.add_artist(circle)
        # save figure
        fig.savefig('state_at_' + str(time.time()) + '_ticks.png', dpi=180, bbox_inches='tight')