#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a != b:
        return (a + b)
    return ((a + b)* 2)

a = 4
b = 3

print(sum_double(a,b))