import discord

from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['h'])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            hembed = discord.Embed(title="\n", description="\n", colour=discord.Color.dark_purple())
            hembed.set_author(name="NextX Bot Commands", icon_url="https://cdn.discordapp.com/avatars/751415029424979988/6160c6b8e76adc207dccdc67791b88f5.webp?size=1024")
            hembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/751415029424979988/6160c6b8e76adc207dccdc67791b88f5.webp?size=1024")            
            hembed.add_field(name=":man_judge:  **Moderation**", value="`$help moderator`", inline=True)
            hembed.add_field(name=":medal: **Levels**", value="`$help levels`", inline=True)
            hembed.add_field(name=":mag:  **Search**", value="`$help search`", inline=True)
            hembed.add_field(name=":musical_note:  **Music**", value="`$help music`", inline=True)
            hembed.add_field(name=":jigsaw:  **Misc**", value="`$help misc`", inline=True)
            hembed.add_field(name=":smile:  **Fun**", value="`$help fun`", inline=True)
            await ctx.send(embed=hembed)
    
    @help.command(aliases=['Moderation', 'Mod', 'mod', 'moderator', 'Moderator'])
    async def moderation(self, ctx):
        hembed = discord.Embed(title="**Moderation Commands**", value=" ", colour=discord.Color.dark_purple())
        hembed.add_field(name="`$clear [count]`", value="Clears specified amount of messages.", inline=False)
        hembed.add_field(name="`$kick [member] (optional reason)`", value="Kicks a member.", inline=False)
        hembed.add_field(name="`$ban [member]`", value="Bans a member.", inline=False)
        hembed.add_field(name="`$unban [member]`", value="Unbans a member.", inline=False)
        hembed.add_field(name="`$userinfo [member]`", value="Gets info about a member.", inline=False)
        hembed.add_field(name="`server`", value="Gets info about server.", inline=False)
        await ctx.send(embed=hembed)

    @help.command(aliases=['Search'])
    async def search(self, ctx):
        hembed = discord.Embed(title="**Search Commands**", colour=discord.Color.dark_purple())
        hembed.add_field(name="`$gsearch [content]`", value="Google searches for you.", inline=False)
        hembed.add_field(name="`$wikisearch [content]`", value="Searches Wikipedia for you.", inline=False)
        hembed.add_field(name="`$ysearch [content] (in development and unavailable)`", value="Searches Youtube for you.", inline=False)
        await ctx.send(embed=hembed)

    @help.command(aliases=['miscellaneous', 'Miscellaneous', 'Misc'])
    async def misc(self, ctx):
        hembed= discord.Embed(title="**Miscellaneous Commands**", colour=discord.Color.dark_purple())
        hembed.add_field(name="`$ping`", value="Gives you the latency.", inline=False)
        hembed.add_field(name="`$loading_anime [process]`", value="Shows you a simple loading animation.", inline=False)
        hembed.add_field(name="`$avatar`", value="Gives you the avatar of a person.", inline=False)
        hembed.add_field(name="`$translate [word]`", value="Translates for you to English.", inline=False)
        hembed.add_field(name="`$urban [word]`", value="A dictionary for you.", inline=False)
        hembed.add_field(name="`$choose [choice1] [choice2]`", value="Makes a decision for you.", inline=False)
        hembed.add_field(name="`$twans`", value="Twans (ツ)", inline=False)
        await ctx.send(embed=hembed)

    @help.command(aliases=['Music', 'sound', 'Sound'])
    async def music(self, ctx):
        hembed = discord.Embed(title="**Music Commands(in development and unavailable)**", colour=discord.Color.dark_purple())
        hembed.add_field(name="`search`", value="Searches music for you", inline=False)
        hembed.add_field(name="`play`", value="Plays a specified song", inline=False)
        hembed.add_field(name="`stop`", value="Stops a song for you", inline=False)
        hembed.add_field(name="`join`", value="Joins the bot to the music channel defined", inline=False)
        hembed.add_field(name="`settings`", value="The bot music settings", inline=False)
        await ctx.send(embed=hembed)

    @help.command(aliases=['level', 'Level', 'Levels'])
    async def levels(self, ctx):
        hembed = discord.Embed(title="**Level Commands(in development and unavailable)**", colour=discord.Color.dark_purple())
        hembed.add_field(name="`levelsys`", value="Sets level system to enabled or disabled.", inline=False)
        hembed.add_field(name="`rank`", value="Gives you your XP level, rank in the server")
        await ctx.send(embed=hembed)

    @help.command()
    async def fun(self, ctx):
        hembed = discord.Embed(title="**Fun Commands**", colour=discord.Color.dark_purple())
        hembed.add_field(name="`$echo`", value="Echos back what you sent the bot.", inline=False)
        hembed.add_field(name="`$8ball [question]`", value="A yes or a no", inline=False)
        hembed.add_field(name="`$joke`", value="A joke for you to laugh.", inline=False)
        await ctx.send(embed=hembed)

def setup(bot):
    bot.add_cog(HelpCog(bot))