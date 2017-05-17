import random
from domain import camera


class State:
    def __init__(self, problem):
        self.cameras = []
        self.problem = problem

    def generate_cams(self, boxes, max_cameras):
        # select one box random number times & put camera in it
        num_cameras = random.randint(1, max_cameras)
        picked_boxes = [random.choice(boxes) for _ in range(num_cameras)]
        for box in picked_boxes:
            cam = camera.Camera(box)
            self.cameras.append(cam)