# jar = ['green', 'red', 'blue']
# n_balls = [1, 10, 2]

import random


def sample_multinomial(keys, weights):
    probability = [w / sum(weights) for w in weights]
    return random.choices(keys, weights=probability, k=1)[0]