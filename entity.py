import json


# base class for living things
class Entity:
    def __init__(self, name, hp, level, max_hp, attack, defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense

    def test_print_info(self):
        print(f'{self.name} has {self.hp} hp remaining')


class Character(Entity):
    all_characters = []

    def __init__(self, name, level, hp, max_hp, attack, defense, xp, gold, mana, inventory, user_id):
        super().__init__(name, level, hp, max_hp, attack, defense)
        self.xp = xp
        self.gold = gold
        self.mana = mana
        self.inventory = inventory
        self.user_id = user_id
        Character.all_characters.append(self)


def save_all_characters():
    chars = [c.__dict__ for c in Character.all_characters]
    json_data = json.dumps(chars, indent=2)
    with open('characters.json', 'w') as outfile:
        outfile.write(json_data)
