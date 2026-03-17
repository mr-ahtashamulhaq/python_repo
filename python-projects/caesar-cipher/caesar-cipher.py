org = "The quick brown fox jumps over the lazy dog"

alphabet = {chr(ord("A") + i): chr(ord("A") + (i + 3) % 26) for i in range(26)}
result = []
for ch in org.upper():
    if (ch.upper()) in alphabet:
        result.append(alphabet[ch])
    else:
        result.append(" ")
print("".join(result))
