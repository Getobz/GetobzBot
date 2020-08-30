import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
bot = commands.Bot(command_prefix="!", description="GETOBZ.PY")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="!cmd", url="https://www.twitch.tv/bot"))
    print("""
    __GETOBZ.PY__
    __Version 1.0__
    __Created By GETOBZ__
          """)

bot.load_extension('cogs.kick')
bot.load_extension('cogs.listban')
bot.load_extension('cogs.ban')
bot.load_extension('cogs.unban')
bot.load_extension('cogs.userinfo')
bot.load_extension('cogs.cmd')

bot.run(os.environ.get("bot_discord_token"))