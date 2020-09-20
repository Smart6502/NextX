import discord
import os
import sys
import sqlite3

from discord.ext import commands

owner_id = 718149776574775387

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['history'])
    async def logs(self, ctx):
        if ctx.message.author.id == owner_id:
            if isinstance(ctx.channel, discord.channel.DMChannel):
                os.chdir('..')
                os.chdir('./logs')
                logfile = open("bot_control.log", "r")
                logcontent = logfile.read()
                await ctx.send("LOGS: ")
                await ctx.send(logcontent)
                logfile.close()

            else: 
                await ctx.send("Incorrect channel.")
        else:
            await ctx.send("You cannot use this command.")  

def setup(bot):
    bot.add_cog(Admin(bot))

