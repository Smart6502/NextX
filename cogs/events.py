import discord
import os 
import sys
import sqlite3
import json

from discord.ext.commands import Cog, command
from time import sleep

conn = sqlite3.connect('./db/serverdata.db')
cur = conn.cursor()

class Events(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['getel'])
    async def get_event_logs(self, ctx):
        await ctx.send(ctx)

    @command()
    async def syscht(self, ctx):
        gid = ctx.guild.system_channel.id
        channel = self.bot.get_channel(gid)
        await channel.send(f"System channel HERE {ctx.message.author.mention}")

def setup(bot):
    bot.add_cog(Events(bot))

