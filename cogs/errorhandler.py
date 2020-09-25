import discord

from discord.ext.commands import Cog, command, errors, MissingRequiredArgument, MissingPermissions

class ErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Missing required args")
        if isinstance(error, MissingPermissions):
            await ctx.send("Missing required permissions")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))