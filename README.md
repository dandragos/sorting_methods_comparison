# Sorting Algorithms Comparison Project
This project aims to compare the performance of five sorting algorithms: Radix Sort, Merge Sort, Shell Sort, Counting Sort, and QuickSort. The goal is to analyze and compare the runtime of these algorithms in different scenarios.

In this repository, besides the python file, you will find a powerpoint presentation of the project.

## Implementation
### Sorting Algorithms
#### Radix Sort:

The implementation uses radix sorting based on digits.
It employs a set of buckets to group elements based on the value of each digit.

#### Merge Sort:

The algorithm divides the list into two parts, sorts them separately, and then merges them.
The implementation uses a recursive function to divide and merge the lists.

#### Shell Sort:

The algorithm uses a variable gap for incremental sorting.
The implementation uses a sequence of steps and rearranges elements based on this gap.

#### Counting Sort:

This algorithm sorts elements based on their frequency.
It calculates the frequency of each element and then reconstructs the sorted list.
#### QuickSort:

The algorithm selects a pivot element and divides the list into two parts: elements smaller and elements larger than the pivot.
The implementation uses recursion to sort these two parts and then concatenates them.

## Generation and Testing
The generate_array function generates an array of length n with random numbers between 0 and max_num.
The run_tests function allows the user to input the number of tests and their parameters.
The generated array is sorted for each algorithm, and the runtime is measured.

## Observations and Conclusions

### Tests Conducted:

Small number of elements, large maximum value (Test 1).
Large number of elements, small maximum value (Test 2).
Large number of elements and small maximum value (Test 3).
Very large number of elements and small maximum value (Test 4).
Small number of elements and small maximum value (Test 5).

### Results:

Counting Sort excels when the number of elements and the maximum value are low (Test 2).
Radix Sort performs well for large datasets with relatively small maximum values (Test 3 and Test 4).
QuickSort works well for moderate-sized datasets but may encounter memory issues for very large datasets.

### General Conclusions:

Algorithms behave differently depending on the characteristics of the dataset.
Counting Sort and Radix Sort are efficient under specific conditions, while QuickSort is suitable for moderate-sized datasets.
Merge Sort and Shell Sort show similar performance and are faster than QuickSort in certain cases.
This project provides a detailed insight into the performance of sorting algorithms in various scenarios and can serve as a basis for further analysis and optimizations.

## How to Run
Clone this repository to your local machine.
Open a terminal and navigate to the project directory.
Run the script using python sorting_comparison.py.
Follow the on-screen prompts to input the number of tests and their parameters.
Feel free to explore and analyze the source code to understand the implementation details and customize the tests according to your needs.


*Made by Dan Dragos*
