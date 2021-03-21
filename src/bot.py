import discord

from discord.ext import commands

import os

from secret import TOKEN

bot = commands.Bot(command_prefix = "!!")

@bot.event
async def on_ready():
    print("Milo bot is online!")
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name = "For Your Requests!"))

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f":white_check_mark: Woof woof - Successfully loaded {extension}")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f":white_check_mark: Woof woof - Successfully unloaded {extension}")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f":white_check_mark: Woof woof - Successfully reloaded {extension}")

for filename in os.listdir('src/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Woof woof - Successfully loaded {filename[:-3]}")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"There was an error whilse running this command! {error}")

bot.run(TOKEN)