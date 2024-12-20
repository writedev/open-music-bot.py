from discord.ext import commands
import discord
import wavelink

class Play(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot