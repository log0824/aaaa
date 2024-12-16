class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)] 
        self.linear_table = [None] * size     
        self.quadratic_table = [None] * size   

    def hash_function(self, key):
        return hash(key) % self.size

    # Phương pháp dây chuyền
    def insert_chaining(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  
                return
        self.table[index].append([key, value])

    def search_chaining(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    # Phương pháp thăm dò tuyến tính
    def insert_linear_probing(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.linear_table[index] is not None:
            if self.linear_table[index][0] == key:
                self.linear_table[index][1] = value 
                return
            index = (index + 1) % self.size
            if index == original_index: 
                raise Exception("Hash table is full")
        self.linear_table[index] = [key, value]

    def search_linear_probing(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.linear_table[index] is not None:
            if self.linear_table[index][0] == key:
                return self.linear_table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    # Phương pháp thăm dò bậc hai
    def insert_quadratic_probing(self, key, value):
        index = self.hash_function(key)
        i = 1
        while self.quadratic_table[index] is not None:
            if self.quadratic_table[index][0] == key:
                self.quadratic_table[index][1] = value 
                return
            index = (self.hash_function(key) + i ** 2) % self.size
            i += 1
            if i > self.size:
                raise Exception("Hash table is full")
        self.quadratic_table[index] = [key, value]

    def search_quadratic_probing(self, key):
        index = self.hash_function(key)
        i = 1
        while self.quadratic_table[index] is not None:
            if self.quadratic_table[index][0] == key:
                return self.quadratic_table[index][1]
            index = (self.hash_function(key) + i ** 2) % self.size
            i += 1
            if i > self.size:
                break
        return None

    # Hiển thị bảng băm
    def display(self):
        print("\nChaining Method:")
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

        print("\nLinear Probing:")
        for i, value in enumerate(self.linear_table):
            print(f"Index {i}: {value}")

        print("\nQuadratic Probing:")
        for i, value in enumerate(self.quadratic_table):
            print(f"Index {i}: {value}")

entries = [("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), ("elderberry", 5), ("fig", 6)]
size = 10

hash_table = HashTable(size)

for key, value in entries:
    hash_table.insert_chaining(key, value)
    hash_table.insert_linear_probing(key, value)
    hash_table.insert_quadratic_probing(key, value)

hash_table.display()

print("\nSearch Results:")
for key, _ in entries:
    print(f"Chaining: Key = {key}, Value = {hash_table.search_chaining(key)}")
    print(f"Linear Probing: Key = {key}, Value = {hash_table.search_linear_probing(key)}")
    print(f"Quadratic Probing: Key = {key}, Value = {hash_table.search_quadratic_probing(key)}")
