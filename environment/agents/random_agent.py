import random

class RandomAgent:
    def select_action(self):
        return random.choice([0, 1, 2])
