import discord
import json
import os
import sys
import time
import psycopg2

from threading import Timer
from discord.ext import commands
from decouple import config
from discord.ext.commands import has_permissions

with open('config.json', 'r') as bootinfo_read:
    boot_info_parse=bootinfo_read.read()

bootinfo_store = json.loads(boot_info_parse)

with open('token.json', 'r') as token_read:
    token_parse=token_read.read()

token_store = json.loads(token_parse)

print("JSON PARSE: PASSED")

#from-bootjson-import-vars

ver = str(bootinfo_store['version'])

print(f"Discord.py Version: {discord.__version__}")
print(f"NextX Bot Version v{ver}")
cd_mapping = commands.CooldownMapping.from_cooldown(12, 20, commands.BucketType.member)
spamming = 0
antispam = True

#----------------------Header------------------------
client = commands.Bot(command_prefix = (('nextx ', '$')))
token = str(token_store['token'])
activity = str(bootinfo_store['playing'])

#load-cogs

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print("Cog: PASSED")

#----------------------Start-------------------------
@client.event
async def on_connect():
    print("Connected. Readying...")
@client.event
async def on_ready():
    iter_length = len(list(client.get_all_members()))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{activity} | {len(client.guilds)} servers & {iter_length} users"))
    print('Bot online')
@client.event
async def on_guild_join(guild):
    iter_length = len(list(client.get_all_members()))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{activity} | {len(client.guilds)} servers & {iter_length} users"))

@client.event
async def on_disconnect():
    print("Disconnected")


client.run(token)




