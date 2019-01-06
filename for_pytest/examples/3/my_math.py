# my_math.py

default_cache = {
    0: 1,
    1: 1
}


def fibonacci(num, cache=default_cache):
    if not isinstance(num, int) or not isinstance(cache, dict):
        raise ValueError("Usage: fibonacci(num=<int>, cahce=<dict>)")

    if num not in cache:
        if num == 0 or num == 1:
            value = 1
        else:
            value = fibonacci(num-2, cache) + fibonacci(num-1, cache)
        cache[num] = value
    return cache[num]