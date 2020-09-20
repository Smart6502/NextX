import discord
import os
import sqlite3

from discord.ext import commands

#CONNECT-TO-DATABASE

os.chdir('db')

connection = sqlite3.connect("serverdata.db")

cursorl = connection.cursor()

owner_id = 718149776574775387

#TO-EXECUTE-COMMANDS

class levelsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getchs(self, ctx):
        if ctx.message.author.id == int(owner_id):
            await ctx.send(connection.total_changes)
        else:
            await ctx.send("Access denied")

def setup(bot):
    bot.add_cog(levelsys(bot))

