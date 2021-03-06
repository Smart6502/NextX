import discord
import os
import pathlib
from discord.ext.commands import Cog, command

#Cog for misc commands
class Misc(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def echo(self, ctx, *args):
        content = ' '.join(args)
        await ctx.send(f"{content}")

    @command()
    async def ping(self,ctx):
        await ctx.send(f':ping_pong: Pong **{round(self.bot.latency * 1000)}ms**')

    @command(aliases=['loading_anime', 'loading animation'])
    async def loading_animation(self, ctx, *args):
        string = ' '.join(args)
        gembed = discord.Embed(title = "**Loading....**", description=str(string))
        gembed.set_thumbnail(url="https://gifimage.net/wp-content/uploads/2017/09/animated-loading-gif-transparent-background-12.gif")
        await ctx.send(embed=gembed)

    @command()
    async def avatar(self,ctx,member: discord.Member):
        embed=discord.Embed(title=f"{member.name}'s avatar", colour=discord.Colour.dark_purple())
        embed.set_image(url=f"{member.avatar_url}")

        if member.mention == "<@751415029424979988>":
            await ctx.send("Hey! You can't do that!")
        else:
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))

