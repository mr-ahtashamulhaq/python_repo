"""You are given two strings s1 and s2. Your task is to identify the characters that appear in either string but not in both (i.e., characters that are unique to one of the strings). Return the result as a sorted string."""
def uncommon_chars(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    
    result = set1.symmetric_difference(set2)
    
    return ''.join(sorted(result))

print(uncommon_chars("characters", "alphabets")) 