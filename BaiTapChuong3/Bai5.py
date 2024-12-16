class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)] 
        self.linear_table = [None] * size    
        self.quadratic_table = [None] * size 

    def hash_function(self, key):
        return key % self.size

    def insert_chaining(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def insert_linear_probing(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.linear_table[index] is not None:
            index = (index + 1) % self.size 
            if index == original_index: 
                raise Exception("Hash table is full")
        self.linear_table[index] = key

    def insert_quadratic_probing(self, key):
        index = self.hash_function(key)
        i = 1
        while self.quadratic_table[index] is not None:
            index = (self.hash_function(key) + i ** 2) % self.size
            i += 1
            if i > self.size: 
                raise Exception("Hash table is full")
        self.quadratic_table[index] = key

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

keys = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
size = 10

hash_table = HashTable(size)

for key in keys:
    hash_table.insert_chaining(key)
    hash_table.insert_linear_probing(key)
    hash_table.insert_quadratic_probing(key)

hash_table.display()
