import math
import mpmath


def F(x): return math.sinh(x) - x + 1


def BISECT(a, b, eps):
    mpmath.mp.dps = 18
    k = 0
    an = a
    bn = b
    r = F(a)
    while True:
        x0 = mpmath.mpf(0.5 * (an + bn))
        y = F(x0)
        if y == 0 or bn - an <= 2 * eps:
            break
        k += 1
        if r * y < 0:
            bn = x0
        else:
            an = x0
            r = y
    return f"прилиженное значение корня {x0} было достигнуто за {k} итераций"


'''a, b, eps = [int(i) for i in input().split()]'''
a, b, eps = [-2, 0, 5 * 10 ** -18]
print(BISECT(a, b, eps))
