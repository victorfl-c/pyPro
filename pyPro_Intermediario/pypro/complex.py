number = -4
def negative(number):
    if number < 0:
        number = number * -1
        new_number = pow(number, 1 / 2)
        return -new_number


def positive (number):
    new_number = pow(number, 1 / 2)
    return new_number

print(negative(number))




