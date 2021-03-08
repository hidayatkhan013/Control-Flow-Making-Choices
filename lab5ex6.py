
def great_42(a,b):
    """
    if a = 42 or b=42 
    return true because one of a and b is 42
    if sum mean a+b is 42 return 42
    if absolute diff is 42 mean abs(a-b)=42
    return true 
    all other cases return false 

    """
    return (a==42 or b==42) or a+b==42 or abs(a-b)==42

print(great_42(0,42))
print(great_42(42,0))
print(great_42(21,21))
print(great_42(3,45))
print(great_42(0,10))
print(great_42(100,102))
print(great_42.__doc__)