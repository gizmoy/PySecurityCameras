from point import Point
from box import Box
from visualization.visualizator import Visualizator


class Problem:
    def __init__(self, config):
        # save all config values
        self.camera_range = config['camera_range']
        self.max_cameras = config['max_cameras']
        self.distance = config['distance']
        self.sigma = config['sigma']
        self.alpha = config['alpha']
        self.beta = config['beta']
        self.h_exp = config['h_exp']
        self.n_exp = config['n_exp']
        self.verbose = config['verbose']
        # init properties
        self.boxes = []
        self.num_checkpoints = 0
        # build boxes
        for box in config['boxes']:
            # retrieve vertex
            vertex_x = box['vertex']['x']
            vertex_y = box['vertex']['y']
            vertex = Point(vertex_x, vertex_y)
            # retrieve width & height
            width = box['width']
            height = box['height']
            # create & add boxes
            new_box = Box(vertex, width, height)
            new_box.generate_checkpoints(self.distance)
            self.boxes.append(new_box)
            # add number of generated checkpoints
            self.num_checkpoints += len(new_box.checkpoints)

    def get_state_cost(self, state, visualize=False, label='none'):
        # get number of unobserved points and number of cameras
        h = self.count_unobserved_checkpoints(state)
        n = len(state.cameras)
        # save number of unobserved points
        state.num_unobserved = h
        # compute state cost
        cost = self.alpha * h**self.h_exp + \
               self.beta  * n**self.n_exp
        # check whether visualization is enabled
        if visualize:
            Visualizator.plot_state(self, state, label)
        # stop observing for next counting
        self.stop_observing()
        # return state cost
        return cost

    def count_unobserved_checkpoints(self, state):
        # count down
        count = self.num_checkpoints
        # check if point is observed by at least one camera and it is - subtract one from count
        for box in self.boxes:
            for point in box.checkpoints:
                for camera in state.cameras:
                    # check first whether checkpoint is observed by another camera and then check reachability
                    if not point.is_observed and camera.can_reach(point):
                        point.is_observed = True
                        count -= 1
        return count

    def stop_observing(self):
        # for all checkpoints set is_observed to false
        for box in self.boxes:
            for point in box.checkpoints:
                point.is_observed = False

