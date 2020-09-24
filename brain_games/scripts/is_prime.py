def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                result = 'no'
                return result
    else:
        result = 'no'
        return result
    result = 'yes'
    return result
