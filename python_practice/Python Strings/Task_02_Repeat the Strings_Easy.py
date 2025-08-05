"""Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter."""
def combo_string(a, b):
    short = a if len(a) < len(b) else b
    longer = a if len(a) > len(b) else b
    return short + longer + short
print(combo_string("HI" , "Ahtasham"))