import discord
import os 
import sys
import sqlite3
import datetime

from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self,ctx):
        embed=discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name="NextX",icon_url="https://nextx.carrd.co/assets/images/image01.jpg?v43565483519951")
        embed.add_field(name=f"Ping: {round(self.bot.latency * 1000)}ms", value="\u200b", inline=False)
        embed.add_field(name=f"Servers: {len(self.bot.guilds)} ", value="\u200b", inline=False)
        embed.set_footer(icon_url="", text="Xenon6502#5188 created this bot")
        await ctx.send(embed=embed)

    @commands.command(aliases=['getstats'])
    async def gstat(self, ctx):
        current_datetime = datetime.datetime.now()
        sembed = discord.Embed(title="Bot Stats", description=f"Current statistics for: **{current_datetime}**", colour=discord.Color.dark_purple())
        sembed.add_field(name="GetCurrentStats", value=f"Watching on **{len(self.bot.guilds)}** servers with a latency of **{round(self.bot.latency * 1000)}ms** :flushed:", inline=True)
        await ctx.send(embed=sembed)

def setup(bot):
    bot.add_cog(Info(bot))

