def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer.")

    prime_list = []
    num = 2

    while len(prime_list) < number_of_primes:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(num)

        num += 1

    return prime_list
