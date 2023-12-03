import os
import sys
import json
import discord
from os import system
from discord.ext import commands

if sys.platform == "linux":
    clear = lambda: system("clear")
else:
    clear = lambda: system("cls")

with open('config.json') as f:
    config = json.load(f)

Token = config.get('Token')
Bot = config.get('Bot')
intents = discord.Intents.all()
intents.members = True
if Bot == True:
    client = commands.Bot(command_prefix="Assault!", case_insensitive=False, self_bot=True, intents=intents)
else:
    client = commands.Bot(command_prefix="Assault!", case_insensitive=False, intents=intents)

@client.event
async def on_connect():
    clear()
    print('''
    logged in as => xanthe#1337
    Bot Token: False
    Scraper Ready: True
    ''')
    try:
        os.remove("info/ids.txt")
        os.remove("info/cids.txt")
        os.remove("info/rids.txt")
    except:
        pass

    guild = input(f"guild: ")
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()

    members_ = 0
    f = open("info/ids.txt", "a+")
    for member in members:
        f.write(f"{member.id}\n")
        members_ += 1
    print(f"Scraped All Members")

    channels = 0
    f = open("info/cids.txt", "a+")
    for channel in guildOBJ.channels:
        f.write(f"{channel.id}\n")
        channels += 1
    print(f"Scraped All Channels")

    roles = 0
    f = open("info/rids.txt", "a+")
    for role in guildOBJ.roles:
        f.write(f"{role.id}\n")
        roles += 1
    print(f"Scraped All Roles")
    print(f"All Scraped Info Was Outputted to the files in info folder")
    print(f'To Load The Nuker, Run Main.py')

try:
    client.run(Token, bot=Bot)
except:
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mInvalid Token!")
    input()
    exit()