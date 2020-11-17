import random
import time

def generate_list(size):
    test = []
    for i in range(size):
        test.append(random.randint(0, size))
    return test

def find(test, id):
    for i in range(len(test)):
        if test[i] == id:
            return True

    return False

start = time.time()
the_list = generate_list(10000000)
finish = time.time() - start

print(f"time to generate list: {finish} s")
start = time.time()
print(find(the_list, random.randint(0, 10000000)))
finish = time.time() - start

print(f"time to find: {finish} s")