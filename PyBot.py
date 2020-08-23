import discord 
import os
from discord.ext import commands, tasks
import secret
from itertools import cycle
import random

client = commands.Bot(command_prefix = '-')
status = cycle(['.help', '@ChocoKeesCake'])

@client.event
async def on_ready():
    change_status.start()
    print ('PyBot is now online.')

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(name='load', hidden='True')
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send(f'ERROR: {type(e).__name__} - {e}')
    else:
        await ctx.send('SUCCESS')

@client.command(name='unload', hidden='True')
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send(f'ERROR: {type(e).__name__} - {e}')
    else:
        await ctx.send('SUCCESS')

@client.command(name='reload', hidden='True')
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send(f'ERROR: {type(e).__name__} - {e}')
    else:
        await ctx.send('SUCCESS')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(secret.discord_key)