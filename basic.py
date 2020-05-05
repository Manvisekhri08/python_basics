import time
import os

while True:
    if os.path.exists("vegetables.txt"):
       with open("vegetables.txt") as myfile:
           print(myfile.read())
    else:
        print("File doesn't exists")

    time.sleep(10)