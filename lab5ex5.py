def squirrel_play(is_summer,temperature):
    """
    is summer: true
    temp:110
    return: flase

    is summer:false
    temp:50
    return: false

    if summer then temp is between 60-100
    if not summer temp is between 60-90

    """
    if temperature>60 and temperature<=90 and (not is_summer):
        return True
    elif temperature>60 and temperature<=100 and is_summer:
        return True
    else:
        return False






print(squirrel_play(True,110))
print(squirrel_play(True,98))
print(squirrel_play(False,70))
print(squirrel_play(False,92))
print(squirrel_play(False,50))


print(squirrel_play.__doc__)