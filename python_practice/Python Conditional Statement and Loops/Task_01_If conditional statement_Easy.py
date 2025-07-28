"""There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false"""
def friends_in_trouble(j_angry, s_angry):
    if ((j_angry and s_angry) == True) or (not j_angry and not s_angry) :
        return True
    else:
        return False

# print(friends_in_trouble(True , False))