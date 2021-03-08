def multiply_uniques(a,b,c):
    """
    set in python always store unique value
    a:3
    b:2
    c:3
    Reult:6 becasue 3 is repated
    

        """
    if a==b==c:
        return 0
    result = 1
    a={a,b,c}
    for i in a:
        result *= i
    return result  


print(multiply_uniques(3,2,3))
print(multiply_uniques(3,3,3))
print(multiply_uniques(3,2,1))
print(multiply_uniques(2,2,10))
print(multiply_uniques.__doc__)