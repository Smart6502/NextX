import discord
import os 
import sys
import sqlite3

from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot








def setup(bot):
    bot.add_cog(Fun(bot))

