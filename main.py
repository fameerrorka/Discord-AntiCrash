# coding: utf-8

import disnake
import asyncio
import json
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('anticrash!'), intents=disnake.Intents.all(), test_guilds=[1189818907419222056], sync_commands=True)

@bot.event
async def on_ready():
    print("Bot Ready")
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.watching, name="Evolution"))

@bot.command(name='load')
async def load(inter, extension):
    if not inter.author.id == 1189818907419222056: 
        return
    try:
        await inter.message.delete()
        bot.load_extension(f'daysanticrashcogs.{extension}')
    except:
        pass

@bot.command(name='unload')
async def unload(inter, extension):
    if not inter.author.id == 1189818907419222056: 
        return
    try: 
        await inter.message.delete()
        bot.unload_extension(f'daysanticrashcogs.{extension}')
    except:
        pass

@bot.command(name='reload')
async def reload(inter, extension):
    if not inter.author.id == 1189818907419222056: 
        return
    try: 
        await inter.message.delete()
        bot.unload_extension(f'daysanticrashcogs.{extension}')
        await asyncio.sleep(4)
        bot.load_extension(f'daysanticrashcogs.{extension}')
    except: 
        pass

if __name__ == '__main__':
    for filename in os.listdir("./daysanticrashcogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"daysanticrashcogs.{filename[:-3]}")
            
bot.run("")