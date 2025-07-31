# Create a class EvenNumbers that takes a limit and returns even numbers from 2 up to that limit. Make it an iterator.
class EvenNumber:
    def __init__(self, limit):
        self.num = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            val = self.num
            self.num += 2
            return val
        else:
            raise StopIteration

c = EvenNumber(20)

for i in c:
    print(i)



# Create your own iterator that returns the characters of a string one by one
# Create an object and use next() manually
class StringIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

s = StringIterator("hello")
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
