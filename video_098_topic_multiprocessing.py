import multiprocessing
import time
# Create a process that prints "Analyzing data..." every 2 seconds (3 times)
def analyze():
    for _ in range(3):
        print("Analyzing data...")
        time.sleep(2)

p1 = multiprocessing.Process(target=analyze)
p1.start()
p1.join()


# Create 2 processes: One prints "Compressing..." 3 times (1 second delay)
# One prints "Encrypting..." 3 times (1.5 second delay)
def compress():
    for _ in range(3):
        print("Compressing...")
        time.sleep(1)

def encrypt():
    for _ in range(3):
        print("Encrypting...")
        time.sleep(1.5)

p2 = multiprocessing.Process(target=compress)
p3 = multiprocessing.Process(target=encrypt)

p2.start()
p3.start()

p2.join()
p3.join()


# Create a process that counts from 1 to 5 with delay, then prints "Done!"
def count():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)
    print("Done!")

p4 = multiprocessing.Process(target=count)
p4.start()
p4.join()
