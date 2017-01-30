import os

count = 0
while (count < 1000):
    inputthree = input("--> ")
    os.system("spotify play " + inputthree)
    count = count + 1
