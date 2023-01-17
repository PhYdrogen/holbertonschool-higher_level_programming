#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    prinf("{} {} {}".format(a, b, add(a, b)))
    prinf("{} {} {}".format(a, b, sub(a, b)))
    prinf("{} {} {}".format(a, b, mul(a, b)))
    prinf("{} {} {}".format(a, b, div(a, b)))
