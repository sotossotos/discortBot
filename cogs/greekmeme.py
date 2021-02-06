from discord.ext.commands import Cog
from discord.ext.commands import command
import asyncio
import discord
class GreekMeme(Cog):
    def __init__(self,bot):
        self.bot=bot
    @Cog.listener()
    async def on_ready(self):
        print("Greek Meme Cog Is Ready")
    @command(pass_context=True,aliases=['kolo'])
    async def kolotripidi(self,ctx, onoma="spyros"):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        print(self.bot.USERS)
        if onoma in self.bot.USERS:
            kolotripidi_atomo=onoma
        else:
            kolotripidi_atomo="spyros"
        if kolotripidi_atomo:
            audio="sound/"+kolotripidi_atomo+".mp3"
        else:
            audio="sound/"+"spyros"+".mp3"
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio(audio),after=lambda e: print("kolotripidi has finished playing"))
            while voice.is_playing():
                await asyncio.sleep(0.1)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/kolotripidi.mp3"),after=lambda e: print("kolotripidi has finished playing"))
    @command(pass_context=True,aliases=['petsokoma','petsokopses'])
    async def petso(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/petsokopses.mp3"),after=lambda e: print("petsokoma has finished playing"))
    @command(pass_context=True,aliases=['ilia','hlia'])
    async def rixto(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/rixto.mp3"),after=lambda e: print("rixto has finished playing"))
    @command(pass_context=True,aliases=['antonis','agapi'])
    async def antoni(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/antonis.mp3"),after=lambda e: print("antoni agapi has finished playing"))
    @command(pass_context=True,aliases=['possible','impossible'])
    async def posibol(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/posibo.mp3"),after=lambda e: print("posibo has finished playing"))
    @command(pass_context=True,aliases=['skoupidi','filos'])
    async def trash(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/skoupidi.mp3"),after=lambda e: print("skoupidi has finished playing"))

    @command(pass_context=True,aliases=['termatismenos','finish'])
    async def terma(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/terma.mp3"),after=lambda e: print("termatismenos has finished playing"))

    @command(pass_context=True,aliases=['vroma'])
    async def vromiari(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/vromiari.mp3"),after=lambda e: print("vromiari has finished playing"))
    @command(pass_context=True,aliases=['antriko'])
    async def antreas(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/antreas.mp3"),after=lambda e: print("antreas has finished playing"))
     
    @command(pass_context=True,aliases=['pateritses'])
    async def anapiri(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/anapiri.mp3"),after=lambda e: print("anapiri has finished playing"))
    
    @command(pass_context=True,aliases=['avgolemonos','augo','avgo'])
    async def augolemonos(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/avgolemonos.mp3"),after=lambda e: print("augo has finished playing"))
    @command(pass_context=True,aliases=['preza'])
    async def prezakias(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/prezakias.mp3"),after=lambda e: print("preza boi has finished playing"))
    @command(pass_context=True,aliases=['rola'])
    async def rolantinio(self,ctx):
        voice=discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("sound/rolantinio.mp3"),after=lambda e: print("rola boi has finished playing"))
    
def setup(bot):
    bot.add_cog(GreekMeme(bot))
