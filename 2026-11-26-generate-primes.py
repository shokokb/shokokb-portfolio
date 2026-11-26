import math
import time

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_naive(n: int) -> list[int]:
    ret = []
    for i in range(2, n + 1):
        if is_prime(i):
            ret.append(i)
    return ret

def generate_primes_seive(n: int) -> list[int]:
    ret = []
    # ①長さ n + 1 の真偟値リストを作る。
    is_prime = [True] * (n + 1)
    # ② 0と1を False にする。
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    # ③ 2から√nまで順番に調べる。
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            # ④ True なら、その数の二乗から倍数を False にする。
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
    # ⑤ 最後に True のインデックスをリストにして返す。
    for i in range(n + 1):
        if is_prime[i]:
            ret.append(i)
    return ret

___main___ = __name__ == "__main__"

if ___main___:
    print("Testing generate_primes_naive generate_primes_seive function:")
    print(f"n generate_primes_naive(n) generate_primes_seive(n)")

    aryn = [100, 1000, 10000, 100000, 1000000]
    for n in aryn:
        start_time = time.perf_counter()
        primes_naive = generate_primes_naive(n)
        end_time = time.perf_counter()
        time_naive = end_time - start_time

        start_time = time.perf_counter()
        primes = generate_primes_seive(n)
        end_time = time.perf_counter()
        time_seive = end_time - start_time

        print(f"{n} {time_naive} {time_seive}")
