import asyncio

# Create an async function that prints "Reminder: Take a break!" every 4 seconds

async def break_reminder():
    while True:
        print("Reminder: Take a break!")
        await asyncio.sleep(4)

# asyncio.run(break_reminder())  # Uncomment this to run only Task 1


# Create two async functions: one that prints "Checking messages..." every 2 seconds
# and another that prints "Syncing files..." every 3 seconds. Run both together.

async def check_messages():
    while True:
        print("Checking messages...")
        await asyncio.sleep(2)

async def sync_files():
    while True:
        print("Syncing files...")
        await asyncio.sleep(3)

# asyncio.run(asyncio.gather(check_messages(), sync_files()))  # Uncomment to run Task 2


# Make an async countdown from 5 to 1, printing each number every 1 second,then print "Go!" at the end.

async def countdown():
    for i in range(5, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print("Go!")

# asyncio.run(countdown())  # Uncomment to run Task 3
