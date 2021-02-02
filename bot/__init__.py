from discord import Intents
from discord.ext.commands import Bot as BotBase

PREFIX="!"

class Bot(BotBase):
    def __init__(self):
        self.PREFIX=PREFIX
        self.ready=False
        self.guild=None
        super().__init__(command_prefix=PREFIX,intents=Intents.all())
    def run(self,version,token):
        self.VERSION=version
        self.TOKEN=token
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
    async def on_message(self,message):
        pass
bot = Bot()