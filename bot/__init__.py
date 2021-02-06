from discord import Intents
from discord.ext.commands import Bot as BotBase
from glob import glob
import discord
import asyncio
import random
USERFILEDIR="users.txt"
PREFIX="!"
COGS=[path.split("\\")[-1][:-3] for path in glob("./cogs/*.py")]
class Bot(BotBase):
    def __init__(self):
        self.PREFIX=PREFIX
        self.ready=False
        self.guild=None
        self.USERS=[]
        self.importUsers()
        super().__init__(command_prefix=PREFIX,intents=Intents.all())
    def setup(self):
        for cog in COGS:
            self.load_extension(f"cogs.{cog}")
            print(f"{cog} cog loaded")
        print("The Setup is complete")
    def run(self,version,token):
        self.VERSION=version
        self.TOKEN=token
        self.setup()
        print("Running Bot...")
        super().run(self.TOKEN,reconnect=True)
    async def on_connect(self):
        print("MalakistiriBot connected")
    async def on_ready(self):
        if not self.ready:
            self.ready=True
            print("MalakistiriBot is ready to Roll Out!")
        else:
            print("MalakistiriBot trying to reconnect")
    async def on_voice_state_update(self,member,before,after):
        voice=discord.utils.get(self.voice_clients, guild=member.guild)
        if before.channel==None and member.name !="MalakistiriBot":
            option=str(random.randint(1,3))
            if member.name == "cynicalsotos":
                option="sotos"
            if voice and not voice.is_playing():
                await asyncio.sleep(2) 
                voice.play(discord.FFmpegPCMAudio("sound/channelJoin"+option+".mp3"),after=lambda e: print("channel join\"options:"+str(option)+"\"finished"))
        #Leaves if nobody is in the voice channel
        if not member.bot and after.channel is None and len([m for m in before.channel.members if m.bot])==1:
            if not [m for m in before.channel.members if not m.bot]:
                await voice.disconnect()
    async def on_message(self,message):
        message.content=message.content.lower()
        await self.process_commands(message)

    def importUsers(self):
        f=open(USERFILEDIR,"r")
        if f.mode=="r":
            content=f.readlines()

            self.USERS=[line.strip() for line in content]

        print("Finished importing users")
bot = Bot()