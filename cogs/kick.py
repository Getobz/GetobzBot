import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, user: discord.User, *reason):
        try:
            reason = " ".join(reason)
            await ctx.guild.kick(user, reason=reason)
            await ctx.send(f"L'utilisateur {user} a été kick du serveur")
        except:
            await ctx.send("L'utilisateur est introuvable.")

def setup(bot):
    bot.add_cog(Kick(bot))