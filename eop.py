# Program to count even and odd numbers in a list

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total Even numbers:", even_count)
print("Total Odd numbers:", odd_count)
