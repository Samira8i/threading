import threading
import random


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def create_file(file):
    with open(file, 'w') as f:
        numbers = [str(random.randint(1, 10)) for _ in range(100)]
        print(numbers)
        f.write('\n'.join(numbers))


t1 = threading.Thread(target=create_file, args=("glamur.txt",))
t1.start()
t1.join()


def find_primes(file, result_file):
    with open(file, 'r') as f:
        numbers = [int(num) for num in f.read().split('\n')]
    primes = []
    for i in numbers:
        if is_prime(i):
            primes.append(i)
    with open(result_file, 'w') as f:
        f.write('\n'.join(map(str, primes)))


def calculate_factorials(file, result_file):
    with open(file, 'r') as f:
        numbers = [int(num) for num in f.read().split('\n')]

    fact = []
    for i in numbers:
        fact.append(factorial(i))

    with open(result_file, 'w') as f:
        f.write('\n'.join(map(str, fact)))


primes_result_file = 'primes_result.txt'
factorials_result_file = 'factorials_result.txt'

t2 = threading.Thread(target=find_primes, args=("glamur.txt", 'primes.txt',))
t3 = threading.Thread(target=calculate_factorials, args=("glamur.txt", 'factorials.txt',))

t2.start()
t3.start()

t2.join()
t3.join()
