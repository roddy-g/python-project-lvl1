def gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    result = number_1 + number_2
    return(result)
