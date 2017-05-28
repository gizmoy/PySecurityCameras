import random
import copy
from domain import camera


class State:
    def __init__(self, problem, cameras=None):
        self.problem = problem
        self.cameras = cameras if cameras else self.generate_cameras()

    def generate_cameras(self):
        # generated cameras
        cameras = []
        # random init number of cameras
        num_cameras = random.randint(1, self.problem.max_cameras)
        # select one box num_cameras times
        picked_boxes = [random.choice(self.problem.boxes) for _ in range(num_cameras)]
        for box in picked_boxes:
            cam = camera.Camera(self.problem, box)
            cameras.append(cam)
        # return generated cameras
        return cameras

    def generate_neighbour(self):
        # clone cameras
        cameras = copy.copy(self.cameras)
        num_cameras = len(cameras)
        # choose mutation type
        if num_cameras == self.problem.max_cameras:
            mutation_type = random.choice(['remove', 'modify'])
        elif num_cameras == 1:
            mutation_type = random.choice(['insert', 'modify'])
        else:
            mutation_type = random.choice(['insert', 'remove', 'modify'])
        # perform mutation depending on selected type
        if mutation_type == 'insert':
            # insert new camera
            box = random.choice(self.problem.boxes)
            new_camera = camera.Camera(self.problem, box)
            cameras.append(new_camera)
        elif mutation_type == 'remove':
            # remove random camera
            cam = random.choice(cameras)
            cameras.remove(cam)
        else:
            # modify position of all cameras
            [c.modify_position() for c in cameras]
        # return new state
        return State(self.problem, cameras)