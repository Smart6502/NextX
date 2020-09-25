import discord
import ascii as asc

from pyfiglet import Figlet, FigletFont
from discord.ext.commands import Cog, command

class Ascii(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def img2txt(self, ctx, url: str = None, columns=30) -> None:
        """Convert image as URL to ascii."""
        if url is None:
            await ctx.send("Specify an URL!")
            return

        output = asc.loadFromUrl(url, columns=columns, color=False)

        await ctx.send(output)

def setup(bot):
    bot.add_cog(Ascii(bot))