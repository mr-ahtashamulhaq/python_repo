import pyttsx3 as py

names = ["ahtsham", "ahmad", "ali"]

for name in names:
  engine = py.init()
  engine.say(f"Shoutout to {name}")
  engine.runAndWait()