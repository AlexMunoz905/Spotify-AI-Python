import os

count = 0
while (count < 1000):
    input = input("--> ")
    os.system("spotify play " + input)
    count = count + 1
