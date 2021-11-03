import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "t", "u", "v", "w", "x",
           "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = int(input("how many characters would you like in your password"))
x = random.randint(0, 1)
for x in range(0, a + 1):
    if x == 0:
        print(random.choice(numbers), end="")
    else:
        print(random.choice(letters), end="")
