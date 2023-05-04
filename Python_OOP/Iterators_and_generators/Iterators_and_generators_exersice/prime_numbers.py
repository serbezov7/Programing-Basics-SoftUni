def get_primes(args):
    for num in args:
        if num <= 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# print(list(get_primes([-2, 0, 0, 1, 1, 0])))