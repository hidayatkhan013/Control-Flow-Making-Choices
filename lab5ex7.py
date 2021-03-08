def blackjack(a,b):
    """
    return closest value to 21
    a=19
    b=20
    return=20
    
    function will search for closest value to 21 
    and will return it
        """
    if (a>21):
        a = 0
    if (b>21):
        b = 0
    if (a>b):
        return a
    else:
        return b





print(blackjack(19,20))
print(blackjack(22,23))
print(blackjack(17,22))
print(blackjack.__doc__)