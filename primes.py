
def primes(number_of_primes):
    list = []
    if number_of_primesb == 0 or number_of_primes==1 or number_of_primes<0:
        return []
    else:
        for i in range(2,number_of_primes):
            if number_of_primes % i:
                list.append(number_of_primes)
            i += 1
    return list
