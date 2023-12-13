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
        embed=discord.Embed(title="About the bot", description="cat_mewo", color=0x449fee, 
        timestamp=datetime.datetime.utcnow())
        embed.set_author(name="小玄", icon_url="https://memes.tw/user-gif/e1b80477f22015d38faf3252336b4760.gif")
        embed.set_thumbnail(url="https://scontent.xx.fbcdn.net/v/t1.15752-9/175711818_157745709601270_3105442292063934979_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=58c789&_nc_ohc=E5HslWhLNkQAX9mmeO_&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=0affc9b2c45c841ad26bb2d4de0332d6&oe=60B48DE0")
        embed.add_field(name="1.command", value="[圖片,[ping,[em", inline=True)
        embed.add_field(name="2.respond", value="hi", inline=True)
        embed.add_field(name="3.回覆", value="嗨", inline=False)
        embed.set_footer(text="Welcome")
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


def setup(bot):
    bot.add_cog(Main(bot))