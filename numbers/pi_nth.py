# from decimal import

# find pi to the nth digit


def estimate_pi(digits, end):
    assert isinstance(digits, int)
    assert isinstance(end, int)
    number = 0
    while len(str(number)) <= digits:
        for k in range(1, end + 1):
            a = (-1) ** k
            b = factorial(6 * k)
            c = (545140134 * k) + 13591409
            d = factorial(3 * k)
            e = factorial(k) ** 3
            f = 640320 ** ((3 * k) + 3/2)
            numb1 = d * e * f
            numb2 = 12 * a * b * c
            number = float(str(numb1 / numb2)[:end])
    return number

# def numerator()


def factorial(input):
    assert isinstance(input, (int, float))
    fact = 1
    for i in range(1, input + 1):
        fact = fact * i
    return fact


def test_estimating_pi():
    pi = estimate_pi(12, 15)
    assert len(str(pi)) == 12, len(str(pi))
