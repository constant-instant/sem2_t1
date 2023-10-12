import time
from best import best
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", rand_string)

def main():
    text = generate_random_string(40000000)
    strr = generate_random_string(5)
    t1 = time.perf_counter()
    best(text, strr)
    t2 = time.perf_counter()
    print(f"Вычисление заняло {t2 - t1:0.8f} секунд")


if __name__ == "__main__":
    main()
