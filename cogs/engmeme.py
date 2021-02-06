from discord.ext.commands import Cog
from discord.ext.commands import command
import discord
class EngMeme(Cog):
    def __init__(self,bot):
        self.bot=bot
    @Cog.listener()
    async def on_ready(self):
        print("EnglishMeme Cog Is Ready")
    @command(pass_context=True,aliases=['thic','fat','boi'])    
    async def thicc(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/THICC.mp3"),after=lambda e: print("thick boi has finished playing"))
def setup(bot):
    bot.add_cog(EngMeme(bot))
