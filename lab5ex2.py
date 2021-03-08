def coupon(amount_spent):
    """
    amount spent:50
    return:4
    Description: when ammount spent is  50 it return 
    8% of 50$
    same calculation for bellow
    Less than $10 No coupon
    Between $10 to $60 8%
    More than $60 to $150 10%
    More than $150 to $210 12%  
    More than $210 14%
    coupon according to input
    """
    if amount_spent<10:
        return 0
    elif amount_spent>=10:
        if amount_spent <=60:
            return (8/100)*amount_spent
        elif amount_spent<=150:
            return (10/100)*amount_spent
        elif amount_spent<=210:
            return (12/100)*amount_spent
        elif amount_spent>210:
            return (14/100)*amount_spent
    return None

print(coupon(50))
print(coupon(61))
print(coupon(160))
print(coupon(200))
print(coupon(500))
print(coupon.__doc__)