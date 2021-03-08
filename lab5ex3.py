def assistance(income,No_of_children):
    """
    income:30000
    no of children:3
    return:4500
    income:15000
    no of children:5
    return:10000
    Descrption: program will return financail assitance 
    according to income and no of children

    """
    if income >=30000 and income <40000 and No_of_children>=3:
        return No_of_children*1500
    elif income>=20000 and income<30000 and No_of_children>=2:
        return No_of_children*1000
    elif income>0 and income<20000:
        return No_of_children*2000
    else:
        return None




print(assistance(30000,3))
print(assistance(25000,3))
print(assistance(15000,5))
print(assistance.__doc__)