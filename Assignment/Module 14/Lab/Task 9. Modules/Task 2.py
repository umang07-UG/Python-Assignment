#Write a Python program to generate random numbers using the random module.

import random


print("Random float (0-1):", random.random())


print("Random integer (10-100):", random.randint(1, 100))


colors = ["red", "green", "blue", "yellow"]
print("Random color:", random.choice(colors))