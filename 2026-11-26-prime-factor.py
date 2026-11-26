def prime_factors(n: int) -> list[int]:
    ret = []
    for i in range(1, n+1):
        while n % i == 0:
            ret.append(i)
            n //= i
    return ret