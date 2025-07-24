import threading
import time
# Create a thread that prints "⏰ Time to study!" every 5 seconds

def study_reminder():
    while True:
        print("⏰ Time to study!")
        time.sleep(5)

t1 = threading.Thread(target=study_reminder)
t1.start()


# Create two threads: One prints "Downloading..." every 3 seconds Another prints "Uploading..." every 4 seconds

def downloading():
    while True:
        print("Downloading...")
        time.sleep(3)

def uploading():
    while True:
        print("Uploading...")
        time.sleep(4)

t2 = threading.Thread(target=downloading)
t3 = threading.Thread(target=uploading)

t2.start()
t3.start()

# Create a thread that counts from 1 to 5 with 1 second delay
# and prints "Finished counting!" at the end

def count():
    for i in range(1, 6):
        print(i)
        time.sleep(1)
    print("Finished counting!")

t4 = threading.Thread(target=count)
t4.start()
