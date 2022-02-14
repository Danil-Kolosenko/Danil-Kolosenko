class MyError(Exception):
    pass

def check_positive(number):

    try:
        a = float(number)
        if a < 0:
            return (f"You input negative number: {a}. Try again.")
    except ValueError:
        return ("Error type: ValueError!")
    except MyError as mr:
        print(mr)
    else:
        return (f"You input positive number: {a}")
