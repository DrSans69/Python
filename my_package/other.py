from random import randint as rand
import random


def fill_input_file(filename: str):
    from sys import set_int_max_str_digits
    from math import factorial
    set_int_max_str_digits(1_000_000_000)
    with open(filename, 'w') as f:
        f.write('\n'.join(list(str(factorial(9999)))))


def fast_pow(x: int, n: int, mul: callable) -> int:
    '''
    Вычисляет x в степени n с использованием функции mul для умножения.

    x: int, основание степени
    n: int, показатель степени (натуральное число)
    mul: Callable[[int, int], int], функция для умножения двух чисел
    '''
    if n == 1:
        return x
    half_n, reminder = divmod(n, 2)
    result = fast_pow(x, half_n, mul)
    result = mul(result, result)
    if reminder:
        result = mul(result, x)
    return result


def create_tests(t: int = 1, filename: str = "input.txt", write_test_number: bool = False):
    '''
    create test

    t
        create t number of tests
    filename
        where it must be writen
    write_test_number
        it says for yourself
    '''
    with open(filename, 'w') as f:
        def write(x: str):
            f.write(x + '\n')
        if write_test_number:
            write(str(t))
        for _ in range(t):
            n = 6
            geers = [rand(1, 7)]
            xs = [0]
            for _ in range(1, n):
                geers.append(rand(1, 7))
                xs.append(geers[-1] + geers[-2] + xs[-1])
            write(str(n))
            write(" ".join(str(i) for i in xs))
            write(" ".join(str(i) for i in geers))


def l_bin_search(l, r, check):
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l


def r_bin_search(l, r, check):
    while l < r:
        m = (l + r + 1) // 2
        if check(m):
            l = m
        else:
            r = m - 1
    return l
