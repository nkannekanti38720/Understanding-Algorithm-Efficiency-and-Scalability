import random

def randomized_quick_sort(arr):
    """Randomized Quicksort algorithm where the pivot is chosen randomly."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Randomly choose pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    return randomized_quick_sort(less_than_pivot) + equal_to_pivot + randomized_quick_sort(greater_than_pivot)

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = randomized_quick_sort(arr)
    print("Sorted array:", sorted_arr)
