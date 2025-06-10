def deterministic_quick_sort(arr):
    """Deterministic Quicksort algorithm where the first element is the pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Use the first element as pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    return deterministic_quick_sort(less_than_pivot) + equal_to_pivot + deterministic_quick_sort(greater_than_pivot)

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = deterministic_quick_sort(arr)
    print("Sorted array:", sorted_arr)
