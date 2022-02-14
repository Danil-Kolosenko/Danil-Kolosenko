class ToSmallNumberGroupError(Exception):
    pass

def check_number_group(number):
    try:
        a = int(number)
        if a <= 10:
            return "We obtain error:Number of your group can't be less than 10"
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError:
        return "We obtain error:Number of your group can't be less than 10"
    else:
        return f"Number of your group {a} is valid"
