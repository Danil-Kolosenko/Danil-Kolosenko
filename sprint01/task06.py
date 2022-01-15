//https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&page=5#

def order(a):
    if sorted(a) == a:
        return "ascending"
    elif sorted(a, reverse=True) == a:
        return "descending"
    else:
        return "not sorted"
