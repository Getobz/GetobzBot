import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

class Unban(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def unban(self, ctx, id: int):
        try:
            user = await bot.fetch_user(id)
            await ctx.guild.unban(user)
            await ctx.send(f"L'utilisateur {id} a été unban.")
        except:
            await ctx.send("L'ID spécifié est introuvable.")

def setup(bot):
    bot.add_cog(Unban(bot))