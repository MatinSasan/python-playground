# good method
def divide1(number, divisor):
    assert divisor != 0, "divided by zero"
    return number / divisor


# bad method
def divide2(number, divisor):
    if divisor == 0:
        raise ValueError('The divisor is 0')
    return number / divisor


print(divide1(2, 0))
