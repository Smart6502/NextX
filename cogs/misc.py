import os
import pathlib
import discord
from discord.ext import commands
import random
from googletrans import Translator
import wikipedia
import urbandictionary as ud
import requests #used to send get request
import psycopg2
from requests import get
from threading import Timer
from time import sleep

#Cog for misc commands
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def github(self, ctx):
        await ctx.send("https://github.com/Smart6502/NextX")
    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(f"{arg}")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f':ping_pong: Pong **{round(self.bot.latency * 1000)}ms**')

    @commands.command(aliases=["8ball","ball"])
    async def _8ball(self,ctx,arg):
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


    async def loading_animation(self, ctx, text):
        gembed = discord.Embed(title = "**Loading....**", description=str(text))
        gembed.set_thumbnail(url="https://gifimage.net/wp-content/uploads/2017/09/animated-loading-gif-transparent-background-12.gif")

    @commands.command()
    async def avatar(self,ctx,member: discord.Member):
        embed=discord.Embed(title=f"{member.name}'s avatar")
        embed.set_image(url=f"{member.avatar_url}")
        await ctx.send(embed=embed)
    @commands.command(aliases=['trans'])
    async def translate(self,ctx,arg,arg2):
        translator = Translator()
        translation = translator.translate(f'{arg}',dest=f"{arg2}")
        embed=discord.Embed(title="Translator", color=0x4f8bed)
        embed.add_field(name="Original Word: ", value=f"`{translation.origin}`", inline=False)
        embed.add_field(name="Translated Word: ", value=f"`{translation.text}`", inline=True)
        await ctx.send(embed=embed)
    @commands.command(aliases=['wikipedia','pedia','wikisearch','wsearch'])
    async def wiki(self,ctx,*,arg):

        search = wikipedia.search(f"{arg}")
        result = search[0]
        id = result.replace('4', '')
        page = wikipedia.page(f"{id}")
        wiki = wikipedia.summary(f"{id}",sentences=1)
        images = page.images
        rand = random.randint(1,20)
        embed=discord.Embed(title="Wikipedia", colour=0xf4eded)
        embed.add_field(name="Search", value=f"`{arg}`", inline=False)
        embed.add_field(name="Result", value=f"`{wiki}`", inline=True)
        embed.set_thumbnail(url=f"{images[rand]}")
        if "svg" in images[rand]:
                embed.set_thumbnail(url=f"{images[random.randint(1,20)]}")
        if "webm" in images[rand]:
                embed.set_thumbnail(url=f"{images[random.randint(1,20)]}")
        if "webp" in images[rand]:
                embed.set_thumbnail(url=f"{images[random.randint(1,20)]}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['ud'])
    async def urban(self,ctx,*,arg):
        defs = ud.define(f'{arg}')
        d = defs[0]
        def_final = d.definition.translate({ord(i): None for i in '[]'})
        embed=discord.Embed(color=0xdf3908)
        embed.set_author(name="Urban DICT",icon_url="https://i.pinimg.com/originals/37/46/41/374641157f9fa2ae904664d6c89b984b.jpg")
        embed.add_field(name="Search", value=f"`{arg}`", inline=False)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/37/46/41/374641157f9fa2ae904664d6c89b984b.jpg")
        embed.add_field(name="Result", value=f"`{def_final}`", inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['gs'])
    async def gsearch(self, ctx, *args):
        
        try: 
            from googlesearch import search 
        except ImportError:  
            print("Google MDLE import error - NotFound") 
        
        # to search 
        query = str(args)

        for j in search(query, tld="com", num=3, stop=3, pause=0):

            await ctx.send(f"**Search result: **")
            await ctx.send(j)
            
        #ERROR FIX PENDING

    @commands.command(aliases=['jokes'])
    async def joke(self,ctx):
        data = requests.get("https://official-joke-api.appspot.com/random_joke")
        rand_joke = data.json()
        str = rand_joke
        embed=discord.Embed(title="Random joke",color=random.randint(0,0xffffff))
        embed.add_field(name=f"Category: {str['type']}", value="\u200b", inline=False)
        embed.add_field(name=f"Joke: {str['setup']}", value=f"{str['punchline']}", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def choose(self,ctx,*,choices):
        choices = choices.split(" ")
        choice = random.choice(choices).strip()
        embed=discord.Embed(title="Choose command", color=random.randint(0, 0xffffff))
        embed.add_field(name="Choices:", value=f"`{choices}`", inline=False)
        embed.add_field(name="Choice:", value=f"`{choice}`", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def twans(self,ctx,*,arg):
        def replaceMultiple(mainString, toBeReplaces, newString):
            for elem in toBeReplaces :
                if elem in mainString :
                    # Replace the string
                    mainString = mainString.replace(elem, newString)

            return mainString
        trans = replaceMultiple(arg, ['l', 'r'] , "w")
        await ctx.send(trans)

    @commands.command()
    async def info(self,ctx):
        embed=discord.Embed(colour=discord.Colour.dark_purple())
        embed.set_author(name="NextX v2.02", icon_url="https://is.gd/TTueo7")
        embed.add_field(name=f"Ping: {round(self.bot.latency * 1000)}ms", value="\u200b", inline=False)
        embed.add_field(name=f"Servers: {len(self.bot.guilds)} ", value="\u200b", inline=False)
        embed.add_field(name=f"Created by: <:Xenon6502:718149776574775387> Xenon6502#5188", value="\u200b", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))

