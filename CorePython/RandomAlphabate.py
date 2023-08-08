#WAP to generate and print a random capital alphabet.
import random
import string
def random_alphabate():
    n=random.choice(string.ascii_uppercase)
    print(n)
random_alphabate()
