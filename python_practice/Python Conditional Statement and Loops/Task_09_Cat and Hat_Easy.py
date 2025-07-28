"""You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets."""
def cat_hat(str):
  ##You need to write complete code this time
  if str.count("cat") == str.count("hat"):
    return True
  else:
    return False
  
# print(cat_hat("catchhaatt"))


