from discord.ext.commands import Cog
from discord.ext.commands import command
import discord
class Basic(Cog):
    def __init__(self,bot):
        self.bot=bot
    @command(pass_content=True)
    async def joinare(self,ctx):
        channel=ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @command(pass_content=True)
    async def leavare(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            print("Bot was told to leave voice channel but wasn't in one")
    
    @Cog.listener()
    async def on_ready(self):
        print("Basic Cog Is Ready")

def setup(bot):
    bot.add_cog(Basic(bot))
