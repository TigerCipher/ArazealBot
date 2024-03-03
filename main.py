import json
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

import entity

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='$', intents=intents)


@client.command(name='foo', help='test command')
async def foo(ctx, arg):
    await ctx.send(arg)


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
