def loginindex():
    with open(file="./apm.7_transformed.txt",mode="r") as f:
        try:
            for i in f:
                s = i.split(":")
                t = i.split(" ")
                if i.lower().find("new session from") > -1:
                    print("session" + " " + s[7] + " " + t[2] + " " + "login" + " " + "from" + " " + t[13])
        except (UnicodeDecodeError):
            print(i)

def usernameindex():
    with open(file="./apm.7_transformed.txt",mode="r") as f:
        try:
            for i in f:
                s = i.split(":")
                t = i.split(" ")
                if i.lower().find("username") > -1:
                    print("session" + " " + s[7] + " " + "username" + " " + t[9])
        except (UnicodeDecodeError):
            print(i)

def logoutindex() :
    with open(file="./apm.7_transformed.txt",mode="r") as f:
        try:
            for i in f:
                s = i.split(":")
                t = i.split(" ")
                if i.lower().find("session deleted due to user inactivity") > -1:
                    print("session" + " " + s[7] + " " + "time" + " " + t[2] + " " + s[8])
        except (UnicodeDecodeError) :
            print(i)


if __name__ == '__main__':
    loginindex()
    usernameindex()
    logoutindex()
