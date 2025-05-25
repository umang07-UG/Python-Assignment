# Generators and Iterators



# 1)  Write a generator function that generates the first 10 even numbers.
def generate_even_numbers():
    return (2 * i for i in range(1, 11))


for even in generate_even_numbers():
    print(even)

print()

#--------------------------------------------------------------------

# 2) Write a Python program that uses a custom iterator to iterate over a list of integers.

numbers = [10, 20, 30, 40, 50]

iterator = (i for i in numbers)


for item in iterator:
    print(item)