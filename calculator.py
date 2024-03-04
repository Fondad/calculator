def calc(x, y, sign):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    elif sign == "/" and y != 0:
        return x / y
