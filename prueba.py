# Ask the user for a number
num = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum of the factors
factors_sum = 0

# Loop through all numbers from 1 to the given number
for i in range(1, num + 1):
    # Check if the current number is a factor of the given number
    if num % i == 0:
        # If it is, add it to the sum of the factors
        factors_sum += i

# Check if the sum of the factors is equal to the given number
if factors_sum == num:
    print(num, "is a perfect number!")
else:
    print(num, "is not a perfect number.")
    