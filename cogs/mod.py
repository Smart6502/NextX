import discord
import sqlite3

from discord.ext import commands
from time import sleep
from datetime import datetime
import random

from discord.ext import commands

owner_id = 718149776574775387

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not isinstance(message.channel, discord.channel.DMChannel):
            channel = message.channel
            words = ['fuck', 'Fuck', 'FUCK', 'bitch', 'Bitch', 'BITCH']
            for x in words:
                if x in message.content:
                    msg = await channel.fetch_message(message.id)
                    await msg.delete()
                    sent = await channel.send("Deleted message containing blacklisted word.")
                    sleep(1)
                    await sent.delete()
            if "how to learn guitar" in message.content:
                await message.channel.send("https://www.youtube.com/watch?v=zUwEIt9ez7M")    
                await message.channel.send("The BASICS - RIFF :rofl:")
        else:
            shamembed = discord.Embed(title="WTF", colour=discord.Color.dark_purple())
            shamembed.add_field(name="Do you think I serve DM's? I DON'T!! So invite me to you server then you can use commands.", value="(ツ)", inline=True)
            await message.channel.send(embed=shamembed)

    @commands.command(aliases=['rm'])
    async def clear(self,ctx, amount : int):
        if commands.has_permissions(manage_messages=True) or ctx.author.id == owner_id:
            await ctx.channel.purge(limit=amount+1)
            sent = await ctx.send(F"Deleted {amount} messages.")
            sleep(1)
            await sent.delete()


    @commands.command(aliases=['b'])
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx,member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044 {member.mention} Banned! Reason: {reason}')

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} kicked! Reason: {reason}')
        await member.send(f'You were kicked from {ctx.message.guild.name}. Reason: {reason}')

    @commands.command(aliases=['m'])
    @commands.has_permissions(administrator=True)
    async def sudo(self,ctx,*,arg):
        if arg == "rm -rf /*":
            amount = 700
            await ctx.channel.purge(limit=amount)

    @commands.command(aliases=['ub'])
    async def unban(self,ctx, *, member):

        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:

            user = ban_entry.user

            await ctx.guild.unban(user)

            await ctx.send(f'{user.mention} Unbanned!.')

    @commands.command(aliases=['user-info','memberinfo'])
    async def userinfo(self,ctx,member: discord.Member):
        if member.guild_permissions.administrator:
            admin = "Yes"
        else:
            admin = "No"
        if member.bot:
            bot = "Yes"
        else:
            bot = "No"
        created = member.created_at
        joined = member.joined_at
        embed=discord.Embed(title=f"{member}")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name="Account created", value=f"{created.strftime('%Y-%m-%d')}", inline=True)
        embed.add_field(name="Nickname", value=f"{member.nick}", inline=True)
        embed.add_field(name="ID", value=f"{member.id}", inline=True)
        embed.add_field(name="Joined at", value=f'{joined.strftime("%Y-%m-%d")}', inline=True)
        embed.add_field(name="Is Admin",value=f'{admin}', inline=True)
        embed.add_field(name="Is Bot",value=f'{bot}', inline=True)
        embed.add_field(name=f'Roles', value=f'{len(member.roles)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['server-info','guild-info'])
    async def server(self,ctx):
        nbr_member=len(ctx.guild.members)
        nbr_text=len(ctx.guild.text_channels)
        nbr_vc=len(ctx.guild.voice_channels)
        created = ctx.guild.created_at
        embed=discord.Embed(title=f"{ctx.guild.name}",color=random.randint(0, 0xffffff))
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.add_field(name="Server created", value=f"{created.strftime('%Y-%m-%d')}", inline=True)
        embed.add_field(name="ID", value=f"{ctx.guild.id}", inline=True)
        embed.add_field(name="Owner",value=f'{ctx.guild.owner}', inline=True)
        embed.add_field(name="Text Channels", value=f"{nbr_text}", inline=True)
        embed.add_field(name="Voice Channels", value=f'{nbr_vc}', inline=True)
        embed.add_field(name="Members",value=f'{nbr_member}', inline=False)
        embed.add_field(name=f'System Channel',value=f'{ctx.guild.system_channel}',inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))

