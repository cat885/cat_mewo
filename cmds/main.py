import discord
from discord.ext import commands
from core.classes import Cog_Extention
import datetime

class Main(Cog_Extention):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About the bot", description="**Cat_mewo is a tesing bot.**\n    by  *小玄*", color=0x449fee, 
        timestamp=datetime.datetime.utcnow())
        embed.set_author(name="小玄", icon_url="https://media.tenor.com/PqcriwZMWGoAAAAi/cecilia-saint-cecilia.gif")
        embed.set_thumbnail(url="https://media1.tenor.com/m/iBmyWFwO0qUAAAAC/anime-smile.gif")
        embed.add_field(name="1.command", value="[圖片,[ping,[em", inline=True)
        embed.add_field(name="2.respond", value="hi")
        embed.set_footer(text="Welcome to test it")
        await ctx.send(embed=embed)
        
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clean(self,ctx, num:int):
        await ctx.channel.purge(limit=num+1)


async def setup(bot):
    await bot.add_cog(Main(bot))