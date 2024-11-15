def add(a, b):
    return a + b 


def divide(a, b):
    if b == 0:
        raise ValueError('на ноль делить нельзя')
    return a/b


# test