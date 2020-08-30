import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

class Listban(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def listban(self, ctx):
        try:
            ids = []
            bans = await ctx.guild.bans()
            for i in bans:
                ids.append(str(i.user.id))
            await ctx.send("Voici la liste des ID banni sur le serveur :")
            await ctx.send("\n".join(ids))
        except:
            await ctx.send("Aucun utilisateur n'a été trouvé dans la liste des membres bannis.")

def setup(bot):
    bot.add_cog(Listban(bot))