import cmath

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate two solutions
    sol1 = (-b - discriminant) / (2 * a)
    sol2 = (-b + discriminant) / (2 * a)

    return sol1, sol2

# Get coefficients from user input
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
solution1, solution2 = solve_quadratic_equation(a, b, c)

# Print the solutions
print("The solutions are {0} and {1}".format(solution1, solution2))
