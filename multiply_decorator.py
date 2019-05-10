def logger(amount):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            print(amount[0])
            amount[0] += 1
            return res

        return wrapper

    return decorator


@logger([0])
def multiply(a, b):
    return a * b


multiply(1, 3)
multiply(1, 3)
multiply(1, 3)
