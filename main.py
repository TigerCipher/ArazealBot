import json
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

import entity
import rpg

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='$', intents=intents)


@client.command(help='roll a dice of a given type')
async def roll(ctx, dice_type: str = commands.parameter(description='d4, d6, d8, d10, d12, d20, d100'),
               num_rolls: int = commands.parameter(description='Number of dice to roll', default=1)):
    result = 0
    rolls = []
    try:
        result, rolls = rpg.roll_dice(dice_type, int(num_rolls))
    except ValueError:
        await ctx.send('Invalid dice type. Valid types are: d4, d6, d8, d10, d12, d20, d100')
        return
    if num_rolls > 1:
        await ctx.send(f'You rolled a {result} from rolls: {rolls}')
    else:
        await ctx.send(f'You rolled a {result}')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


#testPlayer = entity.Character('Billy the Kid', 2, 10, 10, 5, 6, 10, 100,
#                              15, ['sword', 'healing potion', 'rope'], 4353465654645)
# testPlayer2 = entity.Character('John', 5, 20, 20, 10, 5, 100, 1000,
#                               35, ['bow', '20 arrows', 'dagger'], 54563456)

# print('Testing json saving')
# entity.save_all_characters()

print('Testing json reading')
loadedPlayer = entity.load_character_by_id(54563456)
loadedPlayer.test_print_info()

# testPlayer3 = entity.Character('Cynthia', 5, 5, 5, 5, 5, 5, 55, 5, ['apple'], 234)
# print('Saving 3rd character')
# entity.save_all_characters()

# testPlayer3.gold = 65
loadedPlayer.xp += 5

print('Testing saving after modifications')
entity.save_all_characters()

client.run(TOKEN)
