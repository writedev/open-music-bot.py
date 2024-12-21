from discord.ext import commands
import discord
from discord import app_commands
import os
import asyncio
import config_example
import json
import logging
import cogs.tag as tag


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=discord.Intents.all())

    async def on_ready(self):
        print(f"{self.user.name} is ready")
        sync = self.tree.sync()
        print(f"{len(sync)} commands as loaded")

bot = MyBot()

async def load_music_commands():
    for filename in os.listdir("./cogs/music/commands"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.music.commands.{filename[:-3]}")

async def load_music_events():
    for filename in os.listdir("./cogs/music/events"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.music.events.{filename[:-3]}")

if __name__ == "__main__":
    tag.show_tag()
    asyncio.run(load_music_commands())
    asyncio.run(load_music_events())
    bot.run(config_example.DISCORD_BOT_TOKEN, log_handler=handler,  log_level=logging.DEBUG)