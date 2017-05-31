from domain import point as Point, box as Box
from visualization import visualizator as Visualizator


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
        # init lists
        self.boxes = []
        self.log = []
        # build boxes
        for box in config['boxes']:
            # retrieve vertex
            vertex_x = box['vertex']['x']
            vertex_y = box['vertex']['y']
            vertex = Point.Point(vertex_x, vertex_y)
            # retrieve width & height
            width = box['width']
            height = box['height']
            # create & add boxes
            new_box = Box.Box(vertex, width, height)
            new_box.generate_checkpoints(self.distance)
            self.boxes.append(new_box)
        # count number of all checkpoints
        self.num_checkpoints = 0
        for box in self.boxes:
            self.num_checkpoints += len(box.checkpoints)

    def get_state_cost(self, state):
        return self.alpha * self.count_unobserved_checkpoints(state)**self.h_exp + \
               self.beta * len(state.cameras)**self.n_exp

    def count_unobserved_checkpoints(self, state):
        # count down
        count = self.num_checkpoints
        # check if point is observed by at least one camera and then subtract one from count
        for box in self.boxes:
            for point in box.checkpoints:
                for camera in state.cameras:
                    # check first whether checkpoint is observed by another camera and then check reachability
                    if not point.is_observed and camera.can_reach(point):
                        point.is_observed = True
                        count -= 1
        # visualize
        Visualizator.Visualizator.plot(self, state)
        # stop observing for next iteration
        self.stop_observing()
        return count

    def stop_observing(self):
        for box in self.boxes:
            for point in box.checkpoints:
                point.is_observed = False

