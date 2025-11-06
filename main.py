import sys
import URLwork

argData = {"-n": "-", "-u": "-", "-m": "-", "-v": "-", "-o": "-", "-d": "-"}

def ReadArgs():
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if (arg[:1] == "-"):
            if (arg == "-h" and argData[0] == ""):
                ArgsInfo()
            else:
                ParsArgs(arg, sys.argv[i + 1])
    for key in argData:
        if (argData[key] == "-"):
            print(f"\x1b[1;31mError: None value, not all atributes in place\x1b[39;49m")
            return False
    
    return True

def ParsArgs(arg: str, data: str):
    for key in argData:
        if (key == arg):
            argData[arg] = data
            break
    else:
        print(f"\x1b[1;31mError: Incorrect input for {arg}\x1b[39;49m")
        

def GoThrueArgs():
    URLwork.DownloadPakeges(argData["-u"])

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
        URLwork.PrintDependsOfPackege("0ad")
    input("Press enter to exit")