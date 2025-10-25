from asyncio.windows_events import NULL
from contextlib import nullcontext
import sys

argData = [str() for _ in range(6)]

def ReadArgs():
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if (arg[:1] == "-"):
            if (arg == "-n" and argData[0] == ""):
                argData[0] = sys.argv[i + 1]
            elif (arg == "-u" and argData[1] == ""):
                argData[1] = sys.argv[i + 1]
            elif (arg == "-m" and argData[2] == ""):
                argData[2] = sys.argv[i + 1]
            elif (arg == "-v" and argData[3] == ""):
                argData[3] = sys.argv[i + 1]
            elif (arg == "-o" and argData[4] == ""):
                argData[4] = sys.argv[i + 1]
            elif (arg == "-d" and argData[5] == ""):
                argData[5] = sys.argv[i + 1]
            else:
                print(f"\x1b[1;31mError: Incorrect input for {arg}\x1b[39;49m")

def PrintArgs():
    for i in argData:
        print(i)

def ArgsInfo():
    print("""
    -n name
    -u URL of packege
    -m mode
    -v version of packege
    -o output mode
    -d depth of packege tree
    """)

ArgsInfo()
input()