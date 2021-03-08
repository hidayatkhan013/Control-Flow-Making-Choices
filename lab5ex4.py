def bakers_party(bool_flag,No_pastries):
    """
    is weekend:true
    no of pastries:30
    is party: False

    is weekend:true
    no of pastries:50
    is party: True


    """
    if No_pastries>=40 and No_pastries<=60 and (not bool_flag):
        return True
    elif No_pastries>=40 and (bool_flag):
        return True
    else:
        return False    




print(bakers_party(True,30))
print(bakers_party(True,50))
print(bakers_party(True,70))
print(bakers_party(False,30))
print(bakers_party(False,50))
print(bakers_party(False,70))
print(bakers_party.__doc__)