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
from time import sleep

#Cog for misc commands
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *args):
        content = ' '.join(args)
        await ctx.send(f"{content}")

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

    @commands.command(aliases=['loading_anime'])
    async def loading_animation(self, ctx, *args):
        string = ' '.join(args)
        gembed = discord.Embed(title = "**Loading....**", description=str(string))
        gembed.set_thumbnail(url="https://gifimage.net/wp-content/uploads/2017/09/animated-loading-gif-transparent-background-12.gif")
        await ctx.send(embed=gembed)

    @commands.command()
    async def avatar(self,ctx,member: discord.Member):
        embed=discord.Embed(title=f"{member.name}'s avatar", colour=discord.Colour.dark_purple())
        embed.set_image(url=f"{member.avatar_url}")

        if member.mention == "<@751415029424979988>":
            await ctx.send("Hey! You can't do that!")
        else:
            await ctx.send(embed=embed)

    @commands.command(aliases=['trans'])
    async def translate(self,ctx,arg,arg2):
        translator = Translator()
        translation = translator.translate(f'{arg}',dest=f"{arg2}")
        embed=discord.Embed(title="Translator", color=0x4f8bed)
        embed.add_field(name="Original Word: ", value=f"`{translation.origin}`", inline=False)
        embed.add_field(name="Translated Word: ", value=f"`{translation.text}`", inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['wikipedia','wikisearch','wsearch'])
    async def wiki(self,ctx,*args):

        content = ' '.join(args)
        try:
            search = wikipedia.search(f"{content}", suggestion=False)
            timout = False
        except wikipedia.exceptions.DisambiguationError as e:
            search = e.options
        except wikipedia.exceptions.HTTPTimeoutError:
            timout = True
        if timout!=True:
            if len(search) > 0:
                result = search[0]
                id = result.replace('4', '')
                try:
                    page = wikipedia.page(f"{id}") 
                    pagerr=False
                except wikipedia.exceptions.PageError:
                    await ctx.send("PageError: Page Not Found")
                    pagerr=True
                if pagerr==False:
                    wiki = wikipedia.summary(f"{id}",sentences=3, auto_suggest=False)
                    wtitle = page.title
                    images = page.images
                    links = page.links
                    refs = page.references
                    embed=discord.Embed(title="Wikipedia", colour=0xf4eded)
                    embed.add_field(name="Search:", value=f"**`{content}`**", inline=False)
                    embed.add_field(name="Found:", value=f"**`{wtitle}`**")
                    embed.add_field(name="Result:", value=f"{wiki}", inline=False)
                    embed.add_field(name=f"Related and references:", value=f"{links[0]}\n{links[1]}\n{links[2]}\n{refs[0]}\n{refs[1]}", inline=False)
                    embed.set_image(url=f"{images[0]}")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Wiki Page Not Found")
            else:
                await ctx.send("Wiki Page Not Found")
        else:
            await ctx.send("Connection error. Try again after some time.")

    @commands.command(aliases=['ud'])
    async def urban(self,ctx,*args):
        q = ' '.join(args)
        defs = ud.define(f'{q}')
        if len(defs) > 0:
            d = defs[0]
            def_final = d.definition.translate({ord(i): None for i in '[]'})
            uembed=discord.Embed(title=" ", description=" ", color=0xdf3908)
            uembed.set_author(name="Urban Dictionary",icon_url="https://i.pinimg.com/originals/37/46/41/374641157f9fa2ae904664d6c89b984b.jpg")
            uembed.add_field(name="Search", value=f"`{q}`", inline=False)
            uembed.set_thumbnail(url="https://i.pinimg.com/originals/37/46/41/374641157f9fa2ae904664d6c89b984b.jpg")
            uembed.add_field(name="Result", value=f"`{def_final}`", inline=False)
            await ctx.send(embed=uembed)
        else:
            await ctx.send("I couldn't find that query :(")

    @commands.command(aliases=['gs'])
    async def gsearch(self, ctx, *args):
        
        content = ' '.join(args)

        try: 
            from googlesearch import search 
        except ImportError:  
            print("Google MDLE import error - NotFound") 
        
        # to search 
        query = str(content)

        for j in search(query, tld="com", num=4, stop=4, pause=0):

            await ctx.send(f"**Search result: **")
            await ctx.send(j)

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

def setup(bot):
    bot.add_cog(Misc(bot))

