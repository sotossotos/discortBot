import os
from bot import bot
from dotenv import load_dotenv

TOKEN=""
VERSION="0.0.1"
USERFILEDIR="users.txt"
userSet={}
def main():
    importUsers()
    load_dotenv('.env')
    TOKEN=os.getenv('TOKEN')
    bot.run(VERSION,TOKEN)


def importUsers():
    f=open(USERFILEDIR,"r")
    if f.mode=="r":
        content=f.readlines()
        userSet={line.strip() for line in content}
    print("Finished importing users")

if __name__=="__main__":
    main()