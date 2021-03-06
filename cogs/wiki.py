import discord
import wikipedia

from discord.ext.commands import Cog, command
from whapi import search, get_id, get_images

class WikiSearch(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['wikipedia','wikisearch','wsearch'])
    async def wiki(self,ctx,*args):

        content = ' '.join(args)
        try:
            wsearch = wikipedia.search(f"{content}", suggestion=False)
            timeout = False
        except wikipedia.exceptions.DisambiguationError as e:
            wsearch = e.options
        except wikipedia.exceptions.HTTPTimeoutError:
            timeout = True
        if timeout!=True:
            if len(wsearch) > 0:
                result = wsearch[0]
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

    @command(aliases=['howto'])
    async def wikihow(self, ctx, *args):
        content = ' '.join(args)
        content = str(content)
        searches_wh = search(content, 5)
        search_wh = searches_wh[0]
        await ctx.send(search_wh['url'])

def setup(bot):
    bot.add_cog(WikiSearch(bot))
