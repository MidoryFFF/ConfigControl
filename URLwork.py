from urllib.request import urlopen
import gzip
import shutil

packeges = dict()

def DownloadPakeges(packegeName: str):
    universe_URL = packegeName + "/universe/binary-amd64/Packages.gz"
    multiverse_URL = packegeName + "/multiverse/binary-amd64/Packages.gz"

    with urlopen(universe_URL) as response:
        with open("jammy.txt.gz", "wb") as local_file:
            local_file.write(response.read())
        
    with gzip.open("jammy.txt.gz", 'rb') as f_in:
        with open('output_file.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    with open('output_file.txt', "rt", encoding = 'utf-8') as unpacked:
        Parser(unpacked.read())

def Parser(Depends: str):
    listOfВepends = Depends.split("\n\n")
    for i in listOfВepends:
        x = i.split("\n")[0]
        x = x[len("Package: "):]
        packeges[x] = i.split("\n")

def PrintDependsOfPackege(packegeName: str):
    print(i if i[len("Depends: ")] == "Depends: " else "" for i in packeges[packegeName])

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
