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
        pass
        

    @commands.Cog.listener()
    async def on_command_error(self, ctx, *args):
        pass

    @commands.command(aliases=['getel'])
    async def get_event_logs(self, ctx):
        pass

    @commands.command()
    async def syscht(self, ctx):
        gid = ctx.guild.system_channel.id
        channel = self.bot.get_channel(gid)
        await channel.send(f"System channel HERE {ctx.message.author.mention}")

def setup(bot):
    bot.add_cog(Events(bot))

