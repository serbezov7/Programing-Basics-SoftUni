def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""


print(rectangle(2, 10))
