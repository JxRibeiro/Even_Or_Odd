# Simple script to determine if user's input is an even or odd number
# Declaring even and odd variables as lists
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# Function to return last digit
def lastDigit(n):
    return (n % 10)
n = float(input('Input a number and I will say if it is Even or Odd: '))
i =round(lastDigit(n))
if i in even:
    print(n,'is an even number')
else:
    print(n,'is an odd number')
