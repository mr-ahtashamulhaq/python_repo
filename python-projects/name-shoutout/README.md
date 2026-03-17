# Name Shoutout

A Python script that reads out a list of names using text-to-speech.

## What It Does

Loops through a list of names and speaks each one aloud as:
"Shoutout to [name]"

## Usage

Edit the names list in the script:
```python
names = ["Ahtasham", "Ahmad", "Ali"]
```

Then run:
```bash
python name_shoutout.py
```

Your system speakers will read out each name one by one.

## Requirements
```bash
pip install pyttsx3
```

`pyttsx3` works offline and runs on Windows, macOS, and Linux without any
API keys or internet connection.

## What I Learned

- Text-to-speech with `pyttsx3`
- Initializing and running a speech engine
- Looping over a list to trigger sequential audio output