import discord
import os 
import sys
import random
import sqlite3

from discord.ext import commands
from time import sleep

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['dankmeme'])
    async def meme(self, ctx):
        await ctx.send("Memed you HAHAHAHA!")

    #ERROR DUE TO DISCRIMINATOR FIX NEXT TIME

    @commands.command()
    async def hack(self, ctx, member : discord.Member):
        passwords = ['bigpeener123', 'xxbigdxxx', 'pxxxstar1234']
        mostcommon = ['small', 'big', 'thicc', 'dank', 'memes', 'eat']
        sent = await ctx.send(member.mention)
        sleep(0.45)
        await sent.edit(content="Hacking now...")
        sleep(0.75)
        await sent.edit(content=f"Finding discord login... (2FA bypassed)")
        sleep(0.75)
        await sent.edit(content=f"Found:\n**Email**: {member.mention}xxx@gmail.com\n**Password: {random.choice(passwords)}**")
        sleep(0.7)
        await sent.edit(content="Fetching DMs with closest friends (if there are any friends at all)")
        sleep(0.5)
        await sent.edit(content="**Last DM:** Don't frgt to like and subscribe!!")
        sleep(0.75)
        await sent.edit(content="Finding most common word...")
        sleep(0.75)
        await sent.edit(content=f"let mostCommon = {random.choice(mostcommon)}")
        sleep(0.75)
        await sent.edit(content=f"Injecting trojan virus into discriminator {member.mention}")
        sleep(0.75)
        await sent.edit(content="Virus injected, status stolen")
        sleep(0.75)
        await sent.edit(content="Getting Steam info...")
        sleep(0.75)
        await sent.edit(content=f"**IP Address:** 127.0.0.1: {random.randint(1, 6000)}")
        sleep(0.75)
        await sent.edit(content="Reporting account to discord for breaking TOS..")
        sleep(1)
        await sent.edit(content=f"Finished hacking {member.mention}")
        sleep(0.5)
        await sent.edit(content="Command executed with exit code 0")
        await ctx.send("The totally real and dangerous hack is complete")

def setup(bot):
    bot.add_cog(Fun(bot))

