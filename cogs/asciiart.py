import discord
import ascii as asc

from pyfiglet import Figlet, FigletFont
from discord.ext.commands import Cog, command

class Ascii(Cog):
    def __init__(self, bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(Ascii(bot))