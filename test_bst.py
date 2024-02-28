from random import randint
from time import perf_counter

from bst import BalancedTree


MULTIPLIER_PER_ITERATION = 1000
INITIAL_ITERATIONS = MULTIPLIER_PER_ITERATION * 20
RANDOM_MULTIPLIER = 10


def test_data_set(num_of_items=1000):
    iterations = INITIAL_ITERATIONS + num_of_items
    max_value = num_of_items * RANDOM_MULTIPLIER 

    btree = BalancedTree()
    for _ in range(iterations):
        val = randint(0, max_value)
        btree.insert(val)

    time_start = perf_counter()
    for _ in range(1000):
        val = randint(0, max_value)
        btree.insert(val)
        btree.find(val)
        btree.delete(val)
    time_end = perf_counter()
    duration = time_end - time_start
    print('1000 iterations for', num_of_items, duration)
    return (iterations, duration)


def run_iterations(num_of_iterations=100):
    total_duration = []
    for i in range(num_of_iterations):
        num_of_items = (i + 1) * MULTIPLIER_PER_ITERATION
        timings = test_data_set(num_of_items)
        total_duration.append(timings)
    print(total_duration)
    for duration in total_duration:
        print(f'{duration[0]}\t{duration[1]}')


if __name__ == '__main__':
    run_iterations()
