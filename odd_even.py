from threading import Thread
import random

random_number = []

# generating random number
for _ in range(15):
    random_number.append(random.randrange(50))
print(f"random_numbers = {random_number}")


def print_odd():
    odd_numbers = []
    # separating odd numbers
    for item in random_number:
        if item % 2 == 1:
            odd_numbers.append(item)

    # printing odd numbers
    print(f"odd_numbers = {odd_numbers}")


def print_even():
    even_numbers = []
    # separating even numbers
    for item in random_number:
        if item % 2 == 0:
            even_numbers.append(item)

    # printing odd numbers
    print(f"even_numbers = {even_numbers}")


# creating thread objects
odd_thread = Thread(target=print_odd, name="odd")
even_thread = Thread(target=print_even, name="even")

odd_thread.start()
even_thread.start()
