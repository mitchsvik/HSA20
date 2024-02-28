
from random import randint
from time import perf_counter

from counting_sort import counting_sort


MULTIPLIER_PER_ITERATION = 10000
RANDOM_MULTIPLIER = 1


def test_data_set(num_of_items=1000):
    iterations = num_of_items
    max_value = num_of_items * RANDOM_MULTIPLIER

    list_to_sort = []
    for _ in range(iterations):
        val = randint(0, max_value)
        list_to_sort.append(val)

    time_start = perf_counter()
    counting_sort(list_to_sort, 0, max_value)
    time_end = perf_counter()
    duration = time_end - time_start
    print('Sorting', num_of_items, duration)
    return (iterations, duration)


def run_iterations(num_of_iterations=20):
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
