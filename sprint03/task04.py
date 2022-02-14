def divisor(n):
    for i in range(1, int(n / 2) + 2):
        if n % i == 0:
            yield i
        if i > int(n / 2):
                while True:
                    yield None
