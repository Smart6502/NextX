import discord
import os 
import sys
import sqlite3

from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def info(self,ctx):
    embed=discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name="NextX",icon_url="https://is.gd/TTueo7")
    embed.add_field(name=f"Ping: {round(self.client.latency * 1000)}ms", value="\u200b", inline=False)
    embed.add_field(name=f"Servers: {len(self.client.guilds)} ", value="\u200b", inline=False)
    embed.add_field(name=f"Created by: <:Xenon6502:718149776574775387> Xenon6502#5188", value="\u200b", inline=False)
    await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(Info(bot))

