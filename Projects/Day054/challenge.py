"""
The Challenge associated with Day 54:
    Create a decorator function that measures the time it takes to execute any function
"""
import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        difference = end_time - start_time
        print(f'{function.__name__} run speed: {difference}s')

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
