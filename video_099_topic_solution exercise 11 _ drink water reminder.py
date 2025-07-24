# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import time
import winsound

while True:
    print("Time to drink water! 💧")
    winsound.Beep(1000, 1000) 
    time.sleep(3600)

