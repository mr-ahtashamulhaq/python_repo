"""Given a decimal number n (positive) in string format, compute its binary string equivalent and return it. """
def toBinary(n : str):
    num = int(n)
    temp = []
    while num>1:
        remainder = num % 2
        num = num//2
        temp.append(remainder)

    temp.append(num)
    temp.reverse()
    result = ((((str(temp)).replace("[","")).replace("]","")).replace(",","")).replace(" ","")
    return result

print(toBinary("7"))