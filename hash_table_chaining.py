class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a specified size (default: 10)."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining
        
    def _hash(self, key):
        """Hash function to compute the index for a given key."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])  # Append new pair if key doesn't exist
    
    def search(self, key):
        """Search for a value by key in the hash table."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if the key is found
        return None  # Return None if the key is not found
    
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]  # Remove the pair from the list
                return
        print(f"Key '{key}' not found to delete.")  # Handle case where key doesn't exist

    def display(self):
        """Display the entire hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

if __name__ == "__main__":
    # Create a hash table of size 10
    hash_table = HashTable(size=10)
    
    # Insert key-value pairs
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("cherry", 3)
    
    # Display the hash table
    hash_table.display()
    
    # Search for a key
    print(f"Search for 'apple': {hash_table.search('apple')}")
    print(f"Search for 'banana': {hash_table.search('banana')}")
    
    # Delete a key
    hash_table.delete("banana")
    print("After deleting 'banana':")
    hash_table.display()
    
    # Try searching for deleted key
    print(f"Search for 'banana' after deletion: {hash_table.search('banana')}")
