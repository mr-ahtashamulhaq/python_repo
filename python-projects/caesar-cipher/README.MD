# Caesar Cipher

A Python implementation of the Caesar cipher — one of the oldest known substitution ciphers.

## What It Does

Takes a plaintext string, shifts every letter 3 positions forward in the alphabet, and prints the encrypted result. Non-letter characters (spaces, punctuation) are dropped.

## How It Works

The script builds a dictionary that maps each letter to its shifted version using modular arithmetic, so the alphabet wraps around (X → A, Y → B, Z → C). It then loops over each character in the input string, looks it up in that map, and collects the output.

Input:
```
The quick brown fox jumps over the lazy dog
```

Output:
```
WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
```

## Run It
```bash
python caesar_cipher.py
```

No dependencies. Just Python 3.

## What I Learned

- Dictionary comprehensions
- `ord()` and `chr()` for character-to-integer conversion
- Modular arithmetic for wrapping values within a fixed range