"""THEORY LECTURE"""

# TLE stands for Time Limit Exceeded.
# It happens in coding contests or online judges when program takes longer than the allowed time to run.

# Example:
# Given n numbers, print their sum.

# Can give TLE error
n = int(input("enter n"))
nums = list(map(int, input().split()))

total = 0
for i in range(n):
    for j in range(1):
        total += nums[i]

print(total)


# optimized
n = int(input("enter n"))
nums = list(map(int, input().split()))
print(sum(nums))