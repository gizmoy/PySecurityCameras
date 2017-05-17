from domain import point, box


class Problem:
    def __init__(self, config):
        self.camera_range = config['camera_range']
        self.max_cameras = config['max_cameras']
        self.distance = config['distance']
        self.boxes = []
        self.log = []
        # build boxes
        for bx in config['boxes']:
            # retrieve vertex
            vertex_x = bx['vertex']['x']
            vertex_y = bx['vertex']['y']
            vertex = point.Point(vertex_x, vertex_y)
            # retrieve width & height
            width = bx['width']
            height = bx['height']
            # build & add rooms
            b = box.Box(vertex, width, height, self.distance)
            b.generate_check_points(self.distance)
            self.boxes.append(b)