# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Implicitly filter even numbers and square them using a list comprehension
squares_of_even = [n ** 2 for n in numbers if n % 2 == 0]

# Print the result
print(squares_of_even)
