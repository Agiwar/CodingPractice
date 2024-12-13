import random
continues_random_function = random.random


# continues_random_function() if a function that generates a float in [0.0, 1.0)
def dice_roll():
    return int(continues_random_function() * 6) + 1