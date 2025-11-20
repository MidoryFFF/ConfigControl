import sys
from URLwork import Packeges

argData = {"-n": "-", "-u": "-", "-m": "-", "-v": "-", "-o": "-", "-d": "-"}
packs: Packeges = Packeges()

def ReadArgs():
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if (arg[:1] == "-"):
            if (arg == "-h" and argData[0] == ""):
                ArgsInfo()
            elif (ParsArgs(arg, sys.argv[i + 1]) != True):
                return False
    
    flag: bool = True
    for key in argData:
        if (argData[key] == "-"):
            print(f"\x1b[1;31mError: Missing value {key}\x1b[39;49m")
            flag = False
    return flag

def ParsArgs(arg: str, data: str):
    if (arg == "-u" and data[:len("http")] != "http"):
        print(f"\x1b[1;31mError: Incorrect input for {arg}\x1b[39;49m")
        return False
    elif (arg == "-d"):
        if (not(data.isdigit())):
            print(f"\x1b[1;31mError: Incorrect input for {arg} must be intager\x1b[39;49m")
            return False
        elif (int(data) < 1):
            print(f"\x1b[1;31mError: Incorrect input for {arg} must be biger than 0\x1b[39;49m")
            return False
    if (arg == "-"):
        print(f"\x1b[1;31mError: Incorrect input for {arg}\x1b[39;49m")
        return False
    else:
        for key in argData:
            if (key == arg):
                argData[arg] = data
                return True
        else:
            print(f"\x1b[1;31mError: Incorrect argument {arg}\x1b[39;49m")
            return False

def GoThrueArgs():
    packs.DownloadPakeges(argData["-u"])
    packs.PrintDependsOfPackege(argData["-n"])

def PrintArgs():
    for key in argData:
        print(key + " " + argData[key])

def ArgsInfo():
    print("""
    -n name
    -u URL of packege
    -m mode
    -v version of packege
    -o output mode
    -d depth of packege tree
    """)

if (__name__ == "__main__"):
    if (ReadArgs()):
        GoThrueArgs()
    input("Press enter to exit")