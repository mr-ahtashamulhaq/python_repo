# Hydration Reminder

A lightweight Python script that sends a desktop notification every 30 minutes
reminding you to drink water.

## What It Does

Runs in the background in an infinite loop. Every 30 minutes it prints a
message to the console and fires a native desktop notification.

## Usage
```bash
python main.py
```

Keep the terminal open while you work. Press `Ctrl + C` to stop it.

## Requirements
```bash
pip install plyer
```

## Changing the Interval

The wait time is set in seconds. Find this line in `main.py`:
```python
time.sleep(1800)  # 30 minutes
```

Some common values:

| Minutes | Seconds |
|---------|---------|
| 15      | 900     |
| 30      | 1800    |
| 60      | 3600    |

## What I Learned

- Sending cross-platform desktop notifications with `plyer`
- Using `time.sleep()` to control execution intervals
- Building simple background utility scripts