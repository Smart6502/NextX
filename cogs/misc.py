import discord
import os
import pathlib
import json
from discord.ext import commands
import random
from googletrans import Translator
from youtube_search import YoutubeSearch
import wikipedia
import urbandictionary as ud
import requests #used to send get request
from requests import get
from time import sleep

#Cog for misc commands
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *args):
        content = ' '.join(args)
        await ctx.send(f"{content}")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f':ping_pong: Pong **{round(self.bot.latency * 1000)}ms**')

    @commands.command(aliases=['loading_anime'])
    async def loading_animation(self, ctx, *args):
        string = ' '.join(args)
        gembed = discord.Embed(title = "**Loading....**", description=str(string))
        gembed.set_thumbnail(url="https://gifimage.net/wp-content/uploads/2017/09/animated-loading-gif-transparent-background-12.gif")
        await ctx.send(embed=gembed)

    @commands.command()
    async def avatar(self,ctx,member: discord.Member):
        embed=discord.Embed(title=f"{member.name}'s avatar", colour=discord.Colour.dark_purple())
        embed.set_image(url=f"{member.avatar_url}")

        if member.mention == "<@751415029424979988>":
            await ctx.send("Hey! You can't do that!")
        else:
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))

