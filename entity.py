import json
import random
import rpg


# base class for living things
class Entity:
    def __init__(self, name, hp, level, max_hp, attack, defense, xp, gold):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        if defense > 100:
            defense = 100
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def test_print_info(self):
        print(f'{self.name} has {self.hp} hp remaining')

    def fight(self, other):
        chance_hit, _ = rpg.roll_dice('d100')
        if chance_hit >= other.defense:
            damage = self.attack
        else:
            damage = 0
        other.hp -= damage
        return self.attack, other.hp <= 0  # returns damage and whether it was a fatal attack or not


class Character(Entity):
    all_characters = []
    level_cap = 50

    def __init__(self, name, level, hp, max_hp, attack, defense, xp, gold, mana, inventory, user_id):
        super().__init__(name, level, hp, max_hp, attack, defense, xp, gold)
        self.mana = mana
        self.inventory = inventory
        self.user_id = user_id
        Character.all_characters.append(self)


class Enemy(Entity):
    def __init__(self, name, level, max_hp, attack, defense, xp, gold):
        super().__init__(name, max_hp, level, max_hp, attack, defense, xp, gold)


# BEGIN ENEMIES

class Spider(Enemy):
    def __init__(self):
        super().__init__("Spider", 1, 3, 2, 1, 2, 1)


class Rat(Enemy):
    def __init__(self):
        super().__init__("Rat", 1, 2, 1, 1, 1, 1)


# END ENEMIES

def save_all_characters():
    # Try reading and loading existing characters first so no characters not actively loaded are not removed
    try:
        with open('characters.json', 'r') as infile:
            chars = json.load(infile)
    except FileNotFoundError:
        chars = {}

    for c in Character.all_characters:
        user_id_str = str(c.user_id)

        # if an existing character, update
        if user_id_str in chars:
            chars[user_id_str].update(c.__dict__)
        else:
            chars[user_id_str] = c.__dict__

    json_data = json.dumps(chars, indent=2)
    with open('characters.json', 'w') as outfile:
        outfile.write(json_data)


def load_character_by_id(user_id):
    try:
        with open('characters.json', 'r') as infile:
            chars = json.load(infile)
            if str(user_id) in chars:
                char_data = chars[str(user_id)]
                return Character(**char_data)
            else:
                print(f'No character found for user (ID: {user_id})')
                return None
    except FileNotFoundError:
        print('characters.json not found')
        return None
    except json.JSONDecodeError:
        print('Error while decoding characters JSON')
        return None
