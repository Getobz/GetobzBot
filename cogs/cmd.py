import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

class Cmd(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def cmd(self, ctx):
        await ctx.send("Voici les commandes d'aide disponible :\n !help\n !userinfo\n !kick\n !listban\n !ban\n !unban !")

def setup(bot):
    bot.add_cog(Cmd(bot))