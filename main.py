import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

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


client.run(TOKEN)
