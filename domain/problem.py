from domain import point, box


class Problem:
    def __init__(self, config):
        # save all config values
        self.camera_range = config['camera_range']
        self.max_cameras = config['max_cameras']
        self.distance = config['distance']
        self.sigma = config['sigma']
        # init lists
        self.boxes = []
        self.log = []
        # build boxes
        for b in config['boxes']:
            # retrieve vertex
            vertex_x = b['vertex']['x']
            vertex_y = b['vertex']['y']
            vertex = point.Point(vertex_x, vertex_y)
            # retrieve width & height
            width = b['width']
            height = b['height']
            # build & add boxes
            new_box = box.Box(vertex, width, height, self.distance)
            new_box.generate_check_points(self.distance)
            self.boxes.append(new_box)