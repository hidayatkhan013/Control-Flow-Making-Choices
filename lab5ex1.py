def tip(cost,s_level):
    """cost for 20%
    argument1 (100,1)
    Returns: returning 20
    cost for 15%
    argument1 (150,2):
    Returns: 
    int:returning 22.5
    cost for 5%
    argument1 (100,5):
    Returns: 
    int:returning 5
    cost for satisfiction level other than 1,2 and 3
    argument1 (100,5):
    Returns: 
    int:returning None
    """
    tip=0.0
    if s_level==1:
        tip=(20/100)*cost
    elif s_level==2:
        tip=(15/100)*cost
    elif s_level==3:
        tip=(5/100)*cost
    else:
        return None
    return tip
    
print(tip(100,1))
print(tip(150,2))
print(tip(100,3))
print(tip(100,8))
print(tip.__doc__)