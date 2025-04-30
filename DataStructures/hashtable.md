# HASH TABLE or HASH MAP

Readings: 

1. https://web.mit.edu/16.070/www/lecture/lecture_18.pdf

2. https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_lec4/

3. https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_r04/

A **Hash table** is a data structure that stores data in key-value pairs, enabling fast insertion, lookup, and deletion operations. It implements an associative array, also known as a dictionary or map, where each unique key maps to a specific value.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Hash_table_5_0_1_1_1_1_0_SP.svg/380px-Hash_table_5_0_1_1_1_1_0_SP.svg.png)


## How Hash Table works ?


1. Hash Function: When a key is provided, a hash function computes an index (hash code) in an underlying array. This index determines where the value is stored or retrieved

2. Buckets: The array slots are often called buckets. Each bucket can hold one or more key-value pairs, depending on the collision resolution strategy

3. Hashing Process:

    - The key is passed through a hash function.

    - The resulting hash code is mapped to a valid array index (often using modulo operation).

    - The value is stored at this index, alongside its key


![img](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Hash_table_5_0_1_1_1_1_0_LL.svg/500px-Hash_table_5_0_1_1_1_1_0_LL.svg.png)

---

## Where to Use Hash Tables 


Hash tables are highly versatile and efficient data structures used in a wide range of applications that require fast insertion, deletion, and lookup of data.

### 1. Dictionaries and Associative Arrays
Hash tables are the standard way to implement dictionaries (key-value stores) in most programming languages. They allow for rapid retrieval, insertion, and deletion of values by key.

### 2. Caching
Frequently accessed data is stored in hash tables for quick retrieval. This significantly improves performance in systems like:
- Web servers
- Databases
- Operating systems

### 3. Database Indexing
Hash tables are used to build indexes for databases, enabling fast access to records based on key attributes and speeding up query processing.

### 4. Sets and Membership Testing
Hash tables allow constant-time operations for adding, removing, and checking the presence of elements. This is key for:
- Duplicate removal
- Membership tests

### 5. Symbol Tables in Compilers/Interpreters
Compilers and interpreters use hash tables to manage symbol tables, which track variables, functions, and identifiers for efficient code analysis and execution.

### 6. Spell Checkers
Hash tables store dictionaries of valid words, enabling fast spell-checking by quickly verifying if a word exists.

### 7. Caching Computed Values (Memoization)
Expensive computations can be cached in hash tables, avoiding repeated calculations for the same inputs.

### 8. Cryptography and Security
Hash tables are integral in:
- Storing hashed passwords
- Managing digital signatures
- Ensuring data integrity

Hashing is also fundamental in secure password storage and digital signatures.

### 9. Load Balancing
Hashing algorithms and hash tables help distribute requests across servers evenly (e.g., consistent hashing), enabling scalable load balancing in distributed systems.

### 10. Data Deduplication
Storage systems use hash tables to detect and remove duplicate files by comparing file hashes, optimizing space usage.

### 11. Pattern Searching and File Systems
Used in text processing for efficient pattern searching and in file systems for rapid file lookups.

---

## Hash Table Interface


- build(iterable) --> Builds the hash table from an iterable of (key, value) pairs. -> O(n)

- put(key, value) --> Inserts or updates the key with the given value. -> O(1) avg, O(n) worst-case

- get(key) --> Retrieves the value associated with the given key. -> O(1) avg, O(n) worst-case

- remove(key) --> Deletes the key and returns its value if it exists. -> O(1) avg, O(n) worst-case

- contains_key(key) --> Returns True if the key exists in the hash table. -> O(1)

- size() --> Returns the number of key-value pairs. -> O(1)

- is_empty() --> Returns True if the hash table is empty. -> O(1)

- clear() --> Removes all key-value pairs from the table. -> O(1) to O(n)

---

## Implementation of Hash Table


```python
# Hash table implemented in Python

class HashTable:
    def __init__(self, initial_size=8, load_factor=0.75):
        self.size = initial_size
        self.count = 0
        self.load_factor = load_factor
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Basic hash function using Python's built-in hash()
        return hash(key) % self.size

    def _resize(self):
        # Double the size when load factor is exceeded
        new_size = self.size * 2
        new_buckets = [[] for _ in range(new_size)]
        
        # Rehash all existing elements
        for bucket in self.buckets:
            for key, value in bucket:
                new_index = hash(key) % new_size
                new_buckets[new_index].append((key, value))
        
        self.size = new_size
        self.buckets = new_buckets

    def insert(self, key, value):
        # Check if resizing is needed
        if self.count / self.size > self.load_factor:
            self._resize()
        
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Update existing key
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Insert new key
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, value in bucket:
            if k == key:
                return value
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return
        raise KeyError(key)

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.count

```