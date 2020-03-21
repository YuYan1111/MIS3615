def my_abs(number):
    """
    returns the absolute value of any number
    number:an int
    """
    if number<0:
        return -number
    else:
        return number
a=-10
abs_a=my_abs(a)
print(abs_a)
