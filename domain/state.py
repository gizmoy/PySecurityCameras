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
        cameras = [copy.copy(c) for c in self.cameras]
        num_cameras = len(cameras)
        # choose mutation type
        if num_cameras == self.problem.max_cameras:
            mutation_type = random.choice(['remove', 'modify'])
        elif num_cameras == 1:
            mutation_type = random.choice(['insert', 'modify'])
        else:
            mutation_type = random.choice(['insert', 'remove', 'modify'])
        print 'Mutation type: ' + mutation_type
        # perform mutation depending on selected type
        if mutation_type == 'insert':
            # insert new camera
            print 'Choices:'
            for b in self.problem.boxes:
                print '{x: ' + str(b.vertex.x) + ', y: ' + str(b.vertex.y) + '}'
            box = random.choice(self.problem.boxes)
            print 'Selected box: {x: ' + str(box.vertex.x) + ', y: ' + str(box.vertex.y) + '}'
            new_camera = camera.Camera(self.problem, box)
            cameras.append(new_camera)
        elif mutation_type == 'remove':
            # remove random camera
            print 'Choices:'
            for c in cameras:
                print '{x: ' + str(c.pos.x) + ', y: ' + str(c.pos.y) + '}'
            box = random.choice(self.problem.boxes)
            cam = random.choice(cameras)

            print 'Selected camera: {x: ' + str(cam.pos.x) + ', y: ' + str(cam.pos.y) + '}'
            cameras.remove(cam)
        else:
            # modify position of all cameras
            [c.modify_position() for c in cameras]
        # return new state
        return State(self.problem, cameras)