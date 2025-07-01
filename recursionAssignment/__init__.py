# recursion.py

# 1) Recursive multiplication using repeated addition
def recursive_multiply(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + recursive_multiply(a, b - 1)
    else:  # b < 0
        return -recursive_multiply(a, -b)

# 2) Recursive exponentiation
def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * recursive_power(base, exponent - 1)
    else:  # Handle negative exponents (optional)
        return 1 / recursive_power(base, -exponent)

# 3) Recursive countdown from n to 0
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

# 4) Recursive count up from 0 to n
def countup(n, current=0):
    if current > n:
        return
    print(current)
    countup(n, current + 1)

# 5) Recursive string reversal
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

# 6) Recursive prime check
def is_prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# 7) Recursive Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Sample tests (can be removed/commented before submission if required)
if __name__ == "__main__":
    print("1) Multiply 5 * -3:", recursive_multiply(5, -3))
    print("2) 2^4:", recursive_power(2, 4))
    print("3) Countdown from 5:")
    countdown(5)
    print("4) Count up to 5:")
    countup(5)
    print("5) Reverse 'hello':", reverse_string("hello"))
    print("6) Is 17 prime?:", is_prime(17))
    print("7) Fibonacci(6):", fibonacci(6))
