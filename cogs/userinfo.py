import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

class Userinfo(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def userinfo(self, ctx, user=None):
        if user is None:
            user = ctx.author
            member = ctx.message.guild.get_member(user.id)
        else:
            member = ctx.message.mentions[0]
            user = bot.get_user(member.id)
        await ctx.send("Le nom de l'utilisateur est {0.name} \n il a rejoint le discord le {1.joined_at}".format(user, member))

def setup(bot):
    bot.add_cog(Userinfo(bot))