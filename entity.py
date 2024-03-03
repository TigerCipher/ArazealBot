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
