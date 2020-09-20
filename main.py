import discord
import json
import os
import sys
import time
import asyncio

from threading import Timer
from discord.ext import commands
from itertools import cycle
from discord.ext.commands import has_permissions

with open('config.json', 'r') as bootinfo_read:
    boot_info_parse=bootinfo_read.read()

bootinfo_store = json.loads(boot_info_parse)

with open("token.0", "r") as tokenfile:
    token = tokenfile.read()

#from-bootjson-import-vars

ver = str(bootinfo_store['version'])

print(f"Discord.py Version: {discord.__version__}")
print(f"NextX Bot Version v{ver}")
cd_mapping = commands.CooldownMapping.from_cooldown(12, 20, commands.BucketType.member)
spamming = 0
antispam = True

#----------------------Header------------------------
client = commands.Bot(command_prefix = (('nextx ', '$')))
client.remove_command('help')
activity = str(bootinfo_store['playing'])
owner_id = int(bootinfo_store['owner'])

#load-cogs

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Cog {filename[:-3]}: PASSED")



#----------------------Start-------------------------
@client.event
async def on_connect():
    print("Connected. Readying...")
@client.event
async def on_ready():
    iter_length = len(list(client.get_all_members()))
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=f"@NextX.DATABASE | {activity} | {len(client.guilds)} servers & {iter_length} users", type=3))
    print("Bot Online")

@client.event
async def on_guild_join(guild, ctx):
    on_ready()
    gid = ctx.guild.system_channel.id
    channel = client.get_channel(gid)
    await channel.send("Heyo! It's me NextX Bot - The Next Generation Bot for Discord")

@client.event
async def on_disconnect():
    print("Disconnected")

#------------Constant-----------

client.run(token)




