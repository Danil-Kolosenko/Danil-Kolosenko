import cmath

def solve_quadric_equation(a, b, c):
    try:
        a1, b1, c1 = float(a), float(b), float(c)
        D = b**2 - (4*a*c)
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
    except ZeroDivisionError:
        return "Zero Division Error"
    except ValueError:
        return "Could not convert string to float"
    else:
        return f"The solution are x1={x2} and x2={x1}"
