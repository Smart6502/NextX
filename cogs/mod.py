import discord
import sqlite3

from time import sleep
from datetime import datetime
import random

from discord.ext.commands import command, Cog, has_guild_permissions, is_owner

owner_id = 718149776574775387

class Moderation(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        words = []
        for x in words:
            if x in message.content:
                msg = await channel.fetch_message(message.id)
                await msg.delete()
                sent = await channel.send("Deleted message containing blacklisted word.")
                sleep(1)
                await sent.delete()
        if "$how to learn guitar" in message.content:
            await message.channel.send("https://www.youtube.com/watch?v=zUwEIt9ez7M")    
            await message.channel.send("The BASICS - RIFF :rofl:")

    @command(aliases=['rm'])
    async def clear(self,ctx, amount : int):
        if has_guild_permissions(manage_messages=True) or ctx.author.id == owner_id:
            await ctx.channel.purge(limit=amount+1)
            sent = await ctx.send(F"Deleted {amount} messages.")
            sleep(1)
            await sent.delete()

    @command()
    @has_guild_permissions(administrator=True)
    async def nuke(self, ctx):
        try:
            await ctx.channel.clone()
            await ctx.channel.delete()
        except:
            await ctx.send("Failed to nuke channel")

    @command()
    @is_owner()
    async def nukeserver(self, ctx):
        try:
            guild_channels = ctx.guild.channels
            for channel in guild_channels:
                await channel.clone()
                await channel.delete()
        except:
            await ctx.send("Failed to nuke server")

    @command(aliases=['b'])
    @has_guild_permissions(administrator=True)
    async def ban(self,ctx,member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044 {member.mention} Banned! Reason: {reason}')

    @command(aliases=['k'])
    @has_guild_permissions(kick_members=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} kicked! Reason: {reason}')
        await member.send(f'You were kicked from {ctx.message.guild.name}. Reason: {reason}')

    @command(aliases=['m'])
    @has_guild_permissions(administrator=True)
    async def sudo(self,ctx,*,arg):
        if arg == "rm -rf /*":
            amount = 100
            await ctx.channel.purge(limit=amount)

    @command(aliases=['ub'])
    async def unban(self,ctx, *, member):

        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:

            user = ban_entry.user

            await ctx.guild.unban(user)

            await ctx.send(f'{user.mention} Unbanned!.')

    @command(aliases=['user-info','memberinfo'])
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


    @command(aliases=['server-info','guild-info'])
    async def server(self,ctx):
        if not isinstance(ctx.channel, discord.Channel.DMChannel):
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
        else:
            await ctx.send("This is a DM dumbo!")

def setup(bot):
    bot.add_cog(Moderation(bot))

