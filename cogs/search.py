import discord
import json
import urbandictionary as ud
from discord.ext import commands
from googlesearch import search
from youtube_search import YoutubeSearch

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(aliases=['ytsearch'])
    async def ysearch(self, ctx, *args):
        content = ' '.join(args)
        results = YoutubeSearch(content, max_results=1).to_json()
        videos = json.loads(results)
        video_list = videos['videos']
        video_content = video_list[0]
        video_suffix = video_content['url_suffix']
        await ctx.send(f"https://youtube.com{video_suffix}")
        yembed = discord.Embed(title=video_content['title'], description="\u200b", color=discord.Colour.from_rgb(255,0,0))
        yembed.add_field(name="Channel:", value=video_content['channel'], inline=False)
        yembed.add_field(name="Duration:", value=video_content['duration'], inline=False)
        yembed.add_field(name="Views:", value=video_content['views'], inline=False)
        await ctx.send(embed=yembed)

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

def setup(bot):
    bot.add_cog(Search(bot))
