import discord
import os
import json

from discord import Game
from discord.ext import commands, tasks

config = json.load(open('./data/config.json', 'r'))

token = config["token"]

py = commands.AutoShardedBot(command_prefix='.', shard_count=config["shard_count"])

@py.event
async def on_ready():
    print("bot ready")
    game = Game("Something news related will go here")
    await py.change_presence(status=discord.Status.idle, activity=game)

@py.event
async def on_shard_connect(shard_id):
    print(f"shard {shard_id} connected")

@py.event
async def on_shard_disconnect(shard_id):
    print(f"shard {shard_id} disconnected")

@py.event
async def on_shard_resumed(shard_id):
    print(f"shard {shard_id} resumed")

@py.event
async def on_shard_ready(shard_id):
    print(f"shard {shard_id} ready")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        py.load_extension(f'cogs.{filename[:-3]}')

py.run(token)