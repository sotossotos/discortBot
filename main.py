import os
from bot import bot
from dotenv import load_dotenv
from keep_alive import keep_alive

TOKEN=""
VERSION="0.0.1"
def main():
    load_dotenv('.env')
    TOKEN=os.getenv('TOKEN')
    # keep_alive()
    bot.run(VERSION,TOKEN)
if __name__=="__main__":
    main()