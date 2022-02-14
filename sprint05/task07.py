def check_odd_even(number):
    try:
        if number % 2 == 0:
            return "Entered number is even"
    except TypeError:
        return "You entered not a number."
    else:
        return "Entered number is odd"

print(check_odd_even(23))

print(10 % 2 == 0)
