# Terminal News App

A Python script that fetches and displays top headlines by category,
straight in your terminal.

## What It Does

Connects to the NewsAPI, lets you pick a news category, and prints the
latest headlines for it.

## Categories
```
1. Business
2. Entertainment
3. General
4. Health
5. Science
6. Sports
7. Technology
```

## Usage
```bash
python terminal_news.py
```

Pick a number when prompted and the headlines print immediately.

## Example Output
```
---- WELCOME TO NEWS ----

1:  Tesla announces new Gigafactory in Southeast Asia

2:  Apple reports record Q1 earnings

3:  OpenAI releases new model update
```

## Setup

1. Get a free API key from [newsapi.org](https://newsapi.org/)
2. Replace the key in the script:
```python
myapi = "your_api_key_here"
```

3. Install the dependency:
```bash
pip install requests
```

## ⚠️ Note

Never commit your real API key to a public GitHub repository. Move it to
an environment variable before pushing:
```python
import os
myapi = os.environ.get("NEWS_API_KEY")
```

## What I Learned

- Making HTTP requests with the `requests` module
- Working with JSON responses from a REST API
- Building a simple menu-driven terminal app
- Using query parameters in API calls