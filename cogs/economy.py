import discord
import os
import sqlite3

from discord.ext import commands

conn = sqlite3.connect('./db/mainbank.db')

cur = conn.cursor()

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ecotest(self, ctx):
        await ctx.send("Economy test successful.")

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        pass

    @commands.command(aliases=['Work'])
    async def work(self, ctx):
        pass

    @commands.command(aliases=['Job'])
    async def job(self, ctx):
        pass

    @commands.command()
    async def fight(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Economy(bot))