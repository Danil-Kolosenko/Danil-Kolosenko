def day_of_week(day):
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    try:
        a = int(day)
        if a in range(1, 8):
            return day_dict[a]
        else:
            return "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."
