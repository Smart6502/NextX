import discord
import os
import sys
import sqlite3

from discord.ext.commands import Cog, command, is_owner

owner_id = 718149776574775387

class Admin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['history'])
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
    
    @command()
    @is_owner()
    async def leave(self, ctx, *, guild_name):
        guild = discord.utils.get(self.bot.guilds, name=guild_name)
        if guild is None:
            await ctx.send("I don't recognize that guild.")
            return
        await self.bot.leave_guild(guild)
        await ctx.send(f":ok_hand: Left guild: {guild.name} ({guild.id})")

def setup(bot):
    bot.add_cog(Admin(bot))

