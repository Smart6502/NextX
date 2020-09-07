import discord
import os
import sqlite3

from discord.ext import commands

#CONNECT-TO-DATABASE

os.chdir('db')

connection = sqlite3.connect("levelsys.db")

cursor = connection.cursor()

#TO-EXECUTE-COMMANDS

class levelsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testdata(self, ctx):
        ctx.send("Success")
        ctx.send(connection.total_changes)

def setup(bot):
    bot.add_cog(levelsys(bot))

