#Write a generator function that takes a number n and yields numbers from 1 to n
def count_upto(n):
    for i in range(1, n + 1):
        yield i

#Make a generator that takes a number n and yields even numbers from 0 to n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


#Write a generator that takes a string like "hello" and yields one character at a time
def char_gen(word):
    for ch in word:
        yield ch


#Write a generator that counts downward from a number n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
