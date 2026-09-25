# Question 1
import math
radius = float(input("Enter circle radius? "))
area = math.pi * (radius ** 2)
print(f"Circle area = {area:.1f}")
# Question 2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9 / 5) + 32
c_display = int(celsius) if celsius.is_integer() else celsius
print(f"{c_display} (C) = {fahrenheit:.1f} (F)")
# Question 3
num = int(input("Enter a number? "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")
# Question 4
  num = int(input("Enter a number? "))

sum_divisors = 0

if num > 0:
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

if num > 0 and sum_divisors == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")
# Question 5
  colors = ["Yellow", "Blue", "Black", "Red", "White", "Purple"]

favorite_color = input("What is your favorite color? ")
if favorite_color in colors:
    index = colors.index(favorite_color)
    print(f"Your colod is at index {index} in my list")
else:
    print("Sorry, I could not find your color")
# Question 6
  range1 = list(range(0, 7))
print("range1:", *range1, sep=", ")

range2 = list(range(1,11,3))
print("range2:", *range2, sep=", ")

range3 = list(range(5,0,-1))
print("range3:", *range3, sep=", ")

range4 = list(range(6,-3,-2))
print("range4:", *range4, sep=", ")
# Question 7
def remove_dollar_sign(s):
    """Removes all dollar signs from the given string."""
    return s.replace("$", "")

    print(remove_dollar_sign(s="67$"))
# Question 8
  def extract_even(l):
    """Returns a new list containing only even numbers from the input list."""
    return [x for x in l if x % 2 == 0]
#test
print(extract_even([1, 4, 5, -1, 10]))
# Question 9
def factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
      result = 1
      for i in range(n,n + 1):
        result *= i
    return result
# Question 10
def get_divisors(n):
    """Returns a list of all positive divisors of a number n."""
    n = abs(n)
    if n == 0:
        return []

    return [i for i in range(1, n + 1) if n % i == 0]

#test
print(get_divisors(12))
# Question 11
import math


def calculate_distance(p1, p2):
    """Computes the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2)
# Question 12
def print_pattern(m, n, char="* "):
    """Prints a pattern of size m rows by n columns."""
    for _ in range(m):
        print(char * n)
