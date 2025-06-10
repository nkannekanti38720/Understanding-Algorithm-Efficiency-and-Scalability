import random
import time

# --- Randomized Quicksort ---
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Randomly choose pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    return randomized_quick_sort(less_than_pivot) + equal_to_pivot + randomized_quick_sort(greater_than_pivot)

# --- Deterministic Quicksort ---
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Use first element as pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    return deterministic_quick_sort(less_than_pivot) + equal_to_pivot + deterministic_quick_sort(greater_than_pivot)

# --- Hash Table with Chaining ---
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update the value if key already exists
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# --- User Input Functionality ---
def get_quick_sort_input():
    array_size = int(input("Enter the size of the array for sorting: "))
    choice = input("Enter the type of array (random, sorted, reverse-sorted, repeated): ").strip().lower()
    
    if choice == "random":
        return [random.randint(1, 10000) for _ in range(array_size)]
    elif choice == "sorted":
        return sorted([random.randint(1, 10000) for _ in range(array_size)])
    elif choice == "reverse-sorted":
        return sorted([random.randint(1, 10000) for _ in range(array_size)], reverse=True)
    elif choice == "repeated":
        return [random.randint(1, 100) for _ in range(array_size)] * 10  # Repeated values
    else:
        print("Invalid choice. Defaulting to random array.")
        return [random.randint(1, 10000) for _ in range(array_size)]

def get_hash_table_input():
    hash_table = HashTable()
    while True:
        action = input("Enter action for hash table (insert/search/delete/exit): ").strip().lower()
        if action == "insert":
            key = input("Enter the key to insert: ")
            value = input("Enter the value for key '{}': ".format(key))
            hash_table.insert(key, value)
            print(f"Inserted {key}: {value}")
        elif action == "search":
            key = input("Enter the key to search for: ")
            value = hash_table.search(key)
            print(f"Search result for '{key}': {value if value else 'Not Found'}")
        elif action == "delete":
            key = input("Enter the key to delete: ")
            hash_table.delete(key)
            print(f"Deleted {key}")
        elif action == "exit":
            break
        else:
            print("Invalid action. Please choose again.")

# --- Main Program ---
if __name__ == "__main__":
    # --- QuickSort Testing ---
    arr = get_quick_sort_input()
    
    # --- Randomized Quicksort Performance ---
    start = time.time()
    randomized_quick_sort(arr)
    print("Randomized Quicksort time:", time.time() - start)

    # --- Deterministic Quicksort Performance ---
    start = time.time()
    deterministic_quick_sort(arr)
    print("Deterministic Quicksort time:", time.time() - start)
    
    # --- Hash Table Testing ---
    print("\nStarting Hash Table Operations...")
    get_hash_table_input()
