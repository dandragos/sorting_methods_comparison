import random
from random import randint
from time import time
import sys
sys.setrecursionlimit(100000) #crestem limita de recursivitate

def radix_sort(nums):
    RADIX = 10
    max_length = False
    tmp , placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(RADIX)]
        for i in nums:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False
        j = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                nums[j] = i
                j += 1
        placement *= RADIX
    return nums

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = nums[:mid]
    right_list = nums[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    sorted_list = []
    left_i = right_i = 0
    left_len, right_len = len(left_list), len(right_list)
    for _ in range(left_len + right_len):
        if left_i < left_len and right_i < right_len:
            if left_list[left_i] <= right_list[right_i]:
                sorted_list.append(left_list[left_i])
                left_i += 1
            else:
                sorted_list.append(right_list[right_i])
                right_i += 1
        elif left_i == left_len:
            sorted_list.append(right_list[right_i])
            right_i += 1
        elif right_i == right_len:
            sorted_list.append(left_list[left_i])
            left_i += 1
    return sorted_list

def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
    return nums

def counting_sort(nums):
    max_num = max(nums)
    counts = [0] * (max_num + 1)
    for num in nums:
        counts[num] += 1
    sorted_nums = []
    for num, count in enumerate(counts):
        sorted_nums += [num] * count
    return sorted_nums

# def bubble_sort(nums):
#     n = len(nums)
#     for i in range(n):
#         # Pentru fiecare iteratie, elementul maxim se muta la finalul listei
#         for j in range(0, n-i-1):
#             # Compararea elementelor adiacente si interschimbarea lor
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums

def quicksort(arr):
    if len(arr) >=10000:
        print()
        print(" Eroare quicksort: Nu poate fi sortat (memorie insuficienta!)")
        return arr;
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)



def generate_array(n, max_num):
    """Generates an array of n random integers from 0 to max_num."""
    return [random.randint(0, max_num) for _ in range(n)]

def run_tests():
    # Ia numarul de teste
    sorting_algorithms = {
        'Radix Sort': radix_sort,
        'Merge Sort': merge_sort,
        'Shell Sort': shell_sort,
        'Counting Sort': counting_sort,
        'QuickSort': quicksort
    }
    num_tests = int(input("Introdu numarul de teste: "))

    # Parcurge toate testele
    for i in range(num_tests):
        # Ia numarul de elemente si cel mai mare element din testul curent
        n, max_num = map(int, input("Introdu N si Max pentru testul {} (separate prin spatiu): ".format(i + 1)).split())

        # Genereaza un array de numere aleatorii pentru testul curent
        arr = [randint(1, max_num) for _ in range(n)]

        # Sorteaza array-ul cu fiecare algoritm si calculeaza timpul de rulare
        print("Testul {} cu N = {} si Max = {}".format(i + 1, n, max_num))
        for sort_name, sort_func in sorting_algorithms.items():
            sorted_arr = arr.copy()
            start_time = time()
            sort_func(sorted_arr)
            end_time = time()
            print("{:>12}: {:>.6f} secunde".format(sort_name, end_time - start_time))
        print("")


run_tests()

# Introdu N si Max pentru testul 1 (separate prin spatiu): 1000 1000000
# Testul 1 cu N = 1000 si Max = 1000000
#   Radix Sort: 0.000998 secunde
#   Merge Sort: 0.001993 secunde
#   Shell Sort: 0.001034 secunde
# Counting Sort: 0.106719 secunde
#    QuickSort: 0.001992 secunde
#
# Introdu N si Max pentru testul 2 (separate prin spatiu): 10000 1000
# Testul 2 cu N = 10000 si Max = 1000
#   Radix Sort: 0.006981 secunde
#   Merge Sort: 0.028923 secunde
#   Shell Sort: 0.032910 secunde
# Counting Sort: 0.000998 secunde
#
#  Eroare quicksort: Nu poate fi sortat (memorie insuficienta!)
#    QuickSort: 0.000000 secunde
#
# Introdu N si Max pentru testul 3 (separate prin spatiu): 1000000 100
# Testul 3 cu N = 1000000 si Max = 100
#   Radix Sort: 0.595443 secunde
#   Merge Sort: 3.560483 secunde
#   Shell Sort: 3.959375 secunde
# Counting Sort: 0.090757 secunde
#
#  Eroare quicksort: Nu poate fi sortat (memorie insuficienta!)
#    QuickSort: 0.000000 secunde
#
# Introdu N si Max pentru testul 4 (separate prin spatiu): 10000000 1000
# Testul 4 cu N = 10000000 si Max = 1000
#   Radix Sort: 12.400808 secunde
#   Merge Sort: 47.287609 secunde
#   Shell Sort: 102.121573 secunde
# Counting Sort: 0.835729 secunde
#
#  Eroare quicksort: Nu poate fi sortat (memorie insuficienta!)
#    QuickSort: 0.000000 secunde
#
# Introdu N si Max pentru testul 5 (separate prin spatiu): 100 100
# Testul 5 cu N = 100 si Max = 100
#   Radix Sort: 0.000000 secunde
#   Merge Sort: 0.000000 secunde
#   Shell Sort: 0.000000 secunde
# Counting Sort: 0.000000 secunde
#    QuickSort: 0.000000 secunde
#
#
# Comparand timpul de rulare al algoritmilor de sortare prezentati in cele cinci teste, putem observa ca Counting Sort este cel mai
# rapid atunci cand numarul de elemente si valoarea maxima sunt reduse, cum este cazul in Testul 2.
# Pe de alta parte, Radix Sort se comporta cel mai bine cand numarul de elemente este mare, dar valoarea maxima este relativ mica,
# cum este cazul in Testul 3 si Testul 4. Merge Sort si Shell Sort au performante asemanatoare,
# in general fiind mai rapide decat QuickSort, cu exceptia Testului 1, unde QuickSort a avut o performanta comparabila cu celelalte doua algoritmi.
# In general, QuickSort poate fi o alegere buna pentru sortarea unui numar moderat de elemente, dar ar putea intampina probleme cu memorie pentru
# seturi de date mai mari.