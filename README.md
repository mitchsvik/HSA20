# HSA20
Data Structures and Algorithms

This example contains 2 functions: `Balanced Binary Search Tree` and `Counting Sort`

### Self-Balanced Binary Search Tree

Can insert, find, and delete elements

`test_bst` generate `num_of_iterations` (100) datasets of size 20000 - 120000 elements and on 1000 iterations test
speed of insert, find, and delete operations.

Test run displays that the correlation between amount of items and duration of operations is below linear

![Iterations to duration](./bst_iterations_to_duration.png?raw=true "Iterations to duration")

Complexity on avarage is Θ(log(n))

### Counting sort algorithm

Counting sort complexity is N + K where 
K is a range of numbers
N is items count

In case K = N or lover - sorting shows a good performance (200000 items sorted in 0.028 sec)

![Counting sort iterations to duration positive](./counting_sort_iterations_to_duration_pos.png?raw=true "Counting sort iterations to duration")

In case of numbers range K much greater than the amount of items N - sorting doesn't perform well (4000 items sorted in 2.433 sec)

![Counting sort iterations to duration negative](./counting_sort_iterations_to_duration_neg.png?raw=true "Counting sort iterations to duration")
