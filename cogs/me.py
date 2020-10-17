import discord

from discord.ext.commands import Cog, command

class Me(Cog):
    def __init__(self, bot):
        self.bot = bot

    async def authorprojects(self, ctx):
        await ctx.send("Author's Open Source Projects:")
        await ctx.send("https://is.gd/O2jeFH")

def setup(bot):
    bot.add_cog(Me(bot))
