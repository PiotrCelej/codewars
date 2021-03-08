"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

t1 = 42145
t2 = 145263
t3 = 123456789

def descendingOrder(num) :
    s = list(str(num))
    s.sort(reverse=True)
    return int("".join(s))

print(descendingOrder(t1))
print(descendingOrder(0))
print(descendingOrder(51))
print(descendingOrder(987654321))