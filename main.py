import sys
import urllib.request

argData = [str() for _ in range(6)]

universe_URL_mask = "https://archive.ubuntu.com/ubuntu/dists/*/universe/"
multiverse_URL_mask = "https://archive.ubuntu.com/ubuntu/dists/*/multiverse/"

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


"""
URL sample
https://archive.ubuntu.com/ubuntu/dists/*/universe/
https://archive.ubuntu.com/ubuntu/dists/*/multiverse/



test_link = "http://archive.ubuntu.com/ubuntu/dists/jammy/universe/binary-amd64/Packages.gz"

from modulefinder import packagePathMap
from unicodedata import name
from urllib.request import urlopen
import gzip
import shutil

res = dict()
nameBuf = ""
valueBuf = []
buf = []


with urlopen(test_link) as response:
    file_content = response.read()
with open("jammy.txt.gz", "wb") as local_file:
    local_file.write(file_content)
    
with gzip.open("jammy.txt.gz", 'rb') as f_in:
    with open('output_file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

"""


ArgsInfo()
input()