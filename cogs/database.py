import discord
import os
import sqlite3

from discord.ext import commands

#CONNECT-TO-DATABASE

os.chdir('db')

connection = sqlite3.connect("server_data.db")

cursor = connection.cursor()

#TO-EXECUTE-COMMANDS

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        print(connection.total_changes)
        await ctx.send(connection.total_changes)

def setup(bot):
    bot.add_cog(Database(bot))

