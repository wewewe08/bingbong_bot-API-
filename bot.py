import discord
import os
import random
import shutil
import datetime
import time
import asyncio
import logging
import json
import os

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import ConversionError
from dotenv import load_dotenv

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")

logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name = "PYTHON", url = "https://www.twitch.tv/magikeraserer"))
    print("Bot is ready.")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CheckFailure):
        await ctx.send("> **you do not have permissions to use this command.**")
        return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

extensions = ['cogs.ServerInfo', 'cogs.Administrator', 'cogs.Help', 'cogs.Fun', 'cogs.WebRequests']
if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

client.run(DISCORD_KEY)
