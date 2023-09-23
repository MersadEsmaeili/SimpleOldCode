import math

# Input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
delta = b**2 - 4*a*c

# Determine the number of solutions and compute the solutions if applicable
if delta > 0:
    num_solutions = 2
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    solutions = [x1, x2]
elif delta == 0:
    num_solutions = 1
    x = -b / (2*a)
    solutions = [x]
else:
    num_solutions = 0
    solutions = []

# Output the results
print("Discriminant (delta) = ", delta)
print("Number of solutions: ", num_solutions)
if num_solutions > 0:
    print("Solutions: ", solutions)
