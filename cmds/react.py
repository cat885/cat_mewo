import discord
from discord.ext import commands
from core.classes import Cog_Extention
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extention):

    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)


async def setup(bot):
    await bot.add_cog(React(bot))