import discord
import os
import sqlite3

from discord.ext import commands

#CONNECT-TO-DATABASE

os.chdir('db')

connection = sqlite3.connect("levelstate.db")

cursorl = connection.cursor()

#TO-EXECUTE-COMMANDS

class levelsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getchs(self, ctx):
        await ctx.send(connection.total_changes)

def setup(bot):
    bot.add_cog(levelsys(bot))

