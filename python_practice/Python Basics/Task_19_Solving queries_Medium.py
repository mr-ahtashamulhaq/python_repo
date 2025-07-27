"""Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None"."""
a = list(map(int, input("Enter Keys").split()))
b = list(map(str, input("Enter Values").split()))
query = list(map(int, input("enter query 'int' : ").split()))
dict = {}
for i in range(len(a)):
    dict[a[i]] = b[i]
        
ans = []
for key in range(len(query)):
    ########### Write your code below ###############
    # get value for given key
    val = dict.get(query[key])
    ########### Write your code above ###############
    
    # append to ans
    ans.append(val)

# Print ans
print(*ans, sep='\n')