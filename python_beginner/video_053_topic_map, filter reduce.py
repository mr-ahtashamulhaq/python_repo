#Use map() to convert a list of temperatures in Celsius to Fahrenheit and print the new list.

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Temperatures in Fahrenheit:", fahrenheit)



# Use map() to square each element in the list [1, 2, 3, 4, 5] and print the result.

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, nums))
print("Squared numbers:", squared)



#Use filter() to extract all even numbers from the list [5, 8, 12, 15, 18, 21] and print them.

nums = [5, 8, 12, 15, 18, 21]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)



# Use filter() to extract strings with length greater than 4 from the list and print them.

words = ["apple", "bat", "carrot", "dog", "elephant"]
long_words = list(filter(lambda word: len(word) > 4, words))
print("Words with length > 4:", long_words)



# Use reduce() to calculate the product of all numbers in the list [2, 3, 4, 5] and print the result.

from functools import reduce

nums = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print("Product of all numbers:", product)


# Use reduce() with an initializer to calculate the sum of all numbers in the list [1, 2, 3] starting from 10 and print the result.

from functools import reduce

nums = [1, 2, 3]
total = reduce(lambda x, y: x + y, nums, 10)
print("Sum starting from 10:", total)