def factorial(input):
    assert isinstance(input, (int, float))
    fact = 0
    for i in range(0, input + 1):
        fact = fact * i
    return fact