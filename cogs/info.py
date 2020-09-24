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
        embed.add_field(name=f"Ping:", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        embed.add_field(name=f"Servers:", value=f"{len(self.bot.guilds)}", inline=False)
        embed.add_field(name=f"Database:", value="No issues", inline=False)
        embed.add_field(name="\u200b", value="[**Invite me**](https://discord.com/oauth2/authorize?client_id=751415029424979988&permissions=8&scope=bot)\n[**Support Server**](https://discord.gg/mv9XEmk)", inline=False)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/718149776574775387/483127686ff322233d971acff5310175.webp?size=1024", text="Xenon6502#5188 created this bot")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))

