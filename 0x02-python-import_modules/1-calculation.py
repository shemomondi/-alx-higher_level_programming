def perform_calculations():
    """Perform the sum, difference, multiplication, and division of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    sum_result = add(a, b)
    difference_result = sub(a, b)
    multiplication_result = mul(a, b)
    quotient_result = div(a, b)

    return sum_result, difference_result, multiplication_result, quotient_result


if __name__ == "__main__":
    sum_result, difference_result, multiplication_result, quotient_result = perform_calculations()

    print("{} + {} = {}".format(10, 5, sum_result))
    print("{} - {} = {}".format(10, 5, difference_result))
    print("{} * {} = {}".format(10, 5, multiplication_result))
    print("{} / {} = {}".format(10, 5, quotient_result))

