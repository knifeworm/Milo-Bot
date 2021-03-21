import discord

from discord.ext import commands

import os

from secret import TOKEN

bot = commands.Bot(command_prefix="!!")

@bot.event
async def on_ready():
    print("Milo bot is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your requests!"))

bot.run(TOKEN)