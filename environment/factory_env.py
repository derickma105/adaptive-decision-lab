import random

class FactoryEnv:
    def __init__(self):
        self.time = 0

    def step(self, action):
        processing_time = random.randint(1, 10)
        reward = -processing_time
        self.time += 1
        return reward
