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
    try:
        result, rolls = rpg.roll_dice(dice_type, int(num_rolls))
    except ValueError:
        await ctx.send('Invalid dice type. Valid types are: d4, d6, d8, d10, d12, d20, d100')
        return
    if num_rolls > 1:
        await ctx.send(f'You rolled a {result} from rolls: {rolls}')
    else:
        await ctx.send(f'You rolled a {result}')


@client.command(help='Create a character to roleplay in the world of Arazeal')
async def create(ctx, *name: str):
    if name is None or len(name) == 0:
        await ctx.send('You must supply a name')
        return
    user_id = ctx.message.author.id
    c = entity.load_character_by_id(user_id)
    if c is not None:
        await ctx.send(f'You already have a character ({c.name}). You can delete it with `$restart`')
    else:
        full_name = ' '.join(name)
        _ = entity.Character(full_name, 1, 10, 10, 1, 1, 0, 10, 10, [], user_id)
        entity.save_all_characters()
        await ctx.send(f'Your character "{full_name}" has been created')


@client.command(help='test')
async def fake(ctx):
    user_id = ctx.message.author.id
    c = entity.load_character_by_id(user_id)
    if c is not None:
        await ctx.send(f'{c.name} has used the fake power')
    else:
        await ctx.send('You must first create a character with `$create`')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


print('Testing json reading')
loadedPlayer = entity.load_character_by_id(54563456)
loadedPlayer.test_print_info()

loadedPlayer.xp += 5

print('Testing saving after modifications')
entity.save_all_characters()

client.run(TOKEN)
