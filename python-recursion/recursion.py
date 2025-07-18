# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     elif n > 2:
#         return fib(n-1) + fib(n-2)
#from gi.overrides.keysyms import value

#for number in range (500):
 #   print(f"{number} : {fib(number)}")

f_cache = {}
value = 0

"""def fib_2(n) :
    if n in f_cache:
        return f_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib_2(n - 1) + (n - 2)

    f_cache[n] = value
    return value

for n in range (1,10):
    print(n,":", fib_2(n))
    print(f"{n} : {fib_2(n)}")"""

from functools import lru_cache
#least recently used  cache
@lru_cache(maxsize=100)
def fib3(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    elif k > 2:
        return fib3(k - 1) + fib3(k - 2)

for i in range (1, 100):
    print(f"{i} : {fib3(i)}")

