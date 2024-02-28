"""Implement Counting Sort algorithm"""


def counting_sort(arr, min_val, max_val):
    """Counting Sort algorithm"""
    val_range = max_val - min_val + 1
    counters = [0] * val_range
    output = []

    for i in range(len(arr)):
        counters[arr[i] - min_val] += 1

    for i in range(len(counters)):
        val = i + min_val
        count = counters[i]
        for _ in range(count):
            output.append(val)

    return output


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
arr_b = counting_sort(arr, 1, 8)
print("Sorted array is:", arr_b)
