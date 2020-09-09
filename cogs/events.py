import discord
import os 
import sys
import sqlite3

from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        await ctx.send(self.bot.guilds)


    @commands.command(aliases=['getel'])
    async def get_event_logs(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Events(bot))

