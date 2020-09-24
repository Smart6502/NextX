
import discord
import sqlite3

from discord.ext import commands

class SetupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def botsetup(self, ctx, captcha : int, automod : int, antispam : int, levelsys : int):
        guild_id = ctx.guild.id
        consetup = sqlite3.connect('./db/serverdata.db')
        cursor = consetup.cursor()
        for row in cursor.execute("SELECT SETUP FROM ServerData WHERE ID = ?", [guild_id]):
            done = row[0]
            break
        else:
            done = 0

        if done == 1:
            await ctx.send("I think I am setup already :)")
        else:
            cursor.execute("INSERT INTO ServerData(CAPTCHA, AUTOMOD, ANTISPAM, LEVELSYS, SETUP) VALUES (?, ?, ?, ?, ?) WHERE ID = ?", [captcha, automod, antispam, levelsys, 1, guild_id])
            consetup.commit()
            consetup.close()

    @botsetup.error
    async def botsetup_error(self, ctx):
        await ctx.send("Syntax for this command is `botsetup 1/0(captcha) 1/0(automod) 1/0(antispam) 1/0(levelsys)`")
        await ctx.send("If the problem persists, join the help server and ask your question.")

    @commands.command()
    async def wait_for_test(self, message):
        msend = message.channel
        await msend.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == msend

        msg = await self.bot.wait_for('message', check=check)
        await msend.send('Hello {.author}!'.format(msg))

def setup(bot):
    bot.add_cog(SetupCog(bot))
