import time

# Get the current time in seconds since epoch, run a loop with delays, and print the elapsed time.
start_time = time.time()
for i in range(3):
    print("Counting:", i)
    time.sleep(0.5)
end_time = time.time()
print("Elapsed time:", end_time - start_time)


# Create a countdown from 5 to 1 with a 1-second pause between each number.
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Countdown finished.")


# Print the current date and time in a readable formatted string.
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)