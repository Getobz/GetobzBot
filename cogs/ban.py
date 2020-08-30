import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, id, *, reason):
        try:
            id = int(id)
            user = discord.utils.get(ctx.guild.members, id = id)
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(f"L'utilisateur {id} a été banni du serveur")
        except:
            await ctx.send("L'ID spécifié est introuvable.")

def setup(bot):
    bot.add_cog(Moderation(bot))