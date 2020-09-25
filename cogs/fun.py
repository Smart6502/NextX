import discord
import os 
import sys
import random
import sqlite3

from requests import get
from discord.ext.commands import Cog, command
from time import sleep

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['dankmeme'])
    async def meme(self, ctx):
        await ctx.send("Memed you HAHAHAHA!")

    @command(aliases=["8ball","ball"])
    async def _8ball(self,ctx,*args):
        responses = ["It is certain.",

                    "It is decidedly so.",

                    "Without a doubt.",

                    "Yes - definitely.",

                    "You may rely on it.",

                    "As I see it, yes.",

                    "Most likely.",

                    "Outlook good.",

                    "Yes.",

                    "Signs point to yes.",

                    "Reply hazy, try again.",

                    "Ask again later.",

                    "Better not tell you now.",

                    "Cannot predict now.",

                    "Concentrate and ask again.",

                    "Don't count on it.",

                    "My reply is no.",

                    "My sources say no.",

                    "Outlook not so good.",

                    "Very doubtful."
    ]

        await ctx.send(random.choice(responses))

    @command(aliases=['jokes'])
    async def joke(self,ctx):
        data = get("https://official-joke-api.appspot.com/random_joke")
        rand_joke = data.json()
        str = rand_joke
        embed=discord.Embed(title="Random joke",color=random.randint(0,0xffffff))
        embed.add_field(name=f"Category: {str['type']}", value="\u200b", inline=False)
        embed.add_field(name=f"Joke: {str['setup']}", value=f"{str['punchline']}", inline=True)
        await ctx.send(embed=embed)

    @command()
    async def choose(self,ctx,*,choices):
        choices = choices.split(" ")
        choice = random.choice(choices).strip()
        embed=discord.Embed(title="Choose command", color=random.randint(0, 0xffffff))
        embed.add_field(name="Choices:", value=f"`{choices}`", inline=False)
        embed.add_field(name="Choice:", value=f"`{choice}`", inline=True)
        await ctx.send(embed=embed)

    @command()
    async def twans(self,ctx,*,arg):
        def replaceMultiple(mainString, toBeReplaces, newString):
            for elem in toBeReplaces :
                if elem in mainString :
                    # Replace the string
                    mainString = mainString.replace(elem, newString)

            return mainString
        trans = replaceMultiple(arg, ['l', 'r'] , "w")
        await ctx.send(trans)

def setup(bot):
    bot.add_cog(Fun(bot))

