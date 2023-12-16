import discord
from discord.ext import commands
from core.classes import Cog_Extention
import asyncio, json, datetime

class Task(Cog_Extention):

    '''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(837314542853816324)
            while not self.bot.is_closed():
                await self.channel.send('嗨,我是cat_mewo!')
                await asyncio.sleep()#單位:秒

        self.bg_task = self.bot.loop.create_task(interval())
    '''

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel:{self.channel.mention}')




async def setup(bot):
    await bot.add_cog(Task(bot))