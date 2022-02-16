def decorator(func):
    def wrapper():
        print('Commands before func...')
        func()
        print('Commands after func...')
    return wrapper

@decorator
def fun():
    print('Fun working!')

fun()