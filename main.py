import os
TOKEN=""
USERFILEDIR="users.txt"
userSet={}
def main():
    importUsers()
    TOKEN=os.getenv("TOKEN")


def importUsers():
    f=open(USERFILEDIR,"r")
    if f.mode=="r":
        content=f.readlines()
        userSet={line.strip() for line in content}
    print("Finished importing users")
    for user in userSet:
        print(user)

if __name__=="__main__":
    main()