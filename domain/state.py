import random
import copy
from domain import camera


class State:
    def __init__(self, problem, cameras=None):
        self.problem = problem
        self.cameras = cameras if cameras else []

    def generate_cameras(self, boxes, max_cameras):
        num_cameras = random.randint(1, max_cameras)
        # select one box max_cameras times & put camera in it
        picked_boxes = [random.choice(boxes) for _ in range(num_cameras)]
        for box in picked_boxes:
            cam = camera.Camera(box)
            self.cameras.append(cam)

    def generate_neighbour(self):
        # clone cameras
        cameras = copy.copy(self.cameras)
        num_cameras = len(cameras)

        # choose mutation type
        if num_cameras == self.problem.max_cameras:
            mutation_type = random.choice(['rem', 'mod'])
        elif num_cameras == 1:
            mutation_type = random.choice(['add', 'rem'])
        else:
            mutation_type = random.choice(['add', 'rem', 'mod'])

        # perform mutation depending on selected type
        if mutation_type == 'add':
            self.add_camera(cameras)
        elif mutation_type == 'rem':
            self.remove_camera(cameras)
        else:
            self.modify_cameras(cameras)

        return State(self.problem, cameras)

    # adds camera
    def add_camera(self, cameras):
        # choose box and associate it with new camera
        box = random.choice(self.problem.boxes)
        new_camera = camera.Camera(box)
        cameras.append(new_camera)

    # removes random camera
    def remove_camera(self, cameras):
        # remove random camera
        cam = random.choice(cameras)
        cameras.remove(cam)

    # modifies cameras
    def modify_cameras(self, cameras):
        # modify position or change box for every camera
        for cam in cameras:
            #  probability of box change
            p = random.uniform(0, 1)
            if p <= self.problem.box_change_prob:
                boxes_with_no_current = [b for b in self.problem.boxes if b != cam.box]
                box = random.choice(boxes_with_no_current)
                cam.change_box(box)
            else:
                cam.modify_position(self.problem.sigma)