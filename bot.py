import discord
from discord.ext import commands
intents = discord.Intents.all()
import json
import random
import os
import keep_alive

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[', intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
