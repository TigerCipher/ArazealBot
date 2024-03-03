import random


def roll_dice(dice_type, num_rolls=1):
    sides = int(dice_type[1:])
    if dice_type[0] != 'd' or sides not in [4, 6, 8, 10, 12, 20, 100]:
        raise ValueError('Invalid dice type. Valid types are: d4, d6, d8, d10, d12, d20, d100')
    total_value = sum(random.randint(1, sides) for _ in range(num_rolls))
    return total_value
