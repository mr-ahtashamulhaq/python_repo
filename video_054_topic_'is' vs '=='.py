# Check if two identical strings have the same value and same identity

a = "hello"
b = "hello"
print(a == b)
print(a is b)

# Check if two different lists with same content have the same value and identity

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# Check identity when assigning one list to another variable

nums = [4, 5, 6]
copy_nums = nums
print(nums == copy_nums)
print(nums is copy_nums)