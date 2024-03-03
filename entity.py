import json


# base class for living things
class Entity:
    def __init__(self, name, hp, max_hp, attack, defense, xp, gold):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def test_print_info(self):
        print(f'{self.name} has {self.hp} hp remaining')


class Character(Entity):
    all_characters = []

    def __init__(self, name, hp, max_hp, attack, defense, xp, gold):
        super().__init__(name, hp, max_hp, attack, defense, xp, gold)
        Character.all_characters.append(self)


def save_all_characters():
    chars = [c.__dict__ for c in Character.all_characters]
    json_data = json.dumps(chars, indent=2)
    with open('characters.json', 'w') as outfile:
        outfile.write(json_data)
