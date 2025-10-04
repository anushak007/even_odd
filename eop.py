
# Program to count even, odd, and prime numbers in a list

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0
prime_count = 0

# Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if is_prime(num):
        prime_count += 1

print("Total Even numbers:", even_count)
print("Total Odd numbers:", odd_count)
print("Total Prime numbers:", prime_count)
