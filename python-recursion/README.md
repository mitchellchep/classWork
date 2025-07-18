
# python-recursion
Memoization in Python
Memoization in Python is an optimization technique that speeds up programs by caching the results of expensive function calls and reusing them when the same inputs occur again.
 This technique is particularly useful for recursive functions, such as calculating the Fibonacci sequence, where the same values are computed multiple times.

Python provides the functools.lru_cache decorator for memoization, which is a simple lightweight unbounded function cache.
 However, the memoization library offers additional features and solves some drawbacks of functools.lru_cache, such as supporting unhashable types and providing multiple caching algorithms like LFU (Least Frequently Used), FIFO (First In First Out), and TTL (Time-To-Live) support.

Here is an example of a memoized Fibonacci function using a dictionary to cache results:

def memoized_fib(n, cache={}):
    if n in cache:
        result = cache[n]
    elif n <= 2:
        result = 1
        cache[n] = result
    else:
        result = memoized_fib(n - 2) + memoized_fib(n - 1)
        cache[n] = result
    return result
This function checks if the result for a given input n is already in the cache. If it is, the cached result is returned; otherwise, the function computes the result, stores it in the cache, and then returns it.

Using memoization can significantly improve the performance of recursive functions by avoiding redundant calculations.
>>>>>>> 394de56 (My classwork)
