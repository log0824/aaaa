import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(char, freq):
    heap = [HuffmanNode(char[i], freq[i]) for i in range(len(char))]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merge = HuffmanNode(None, left.freq + right.freq)
        merge.left = left
        merge.right = right

        heapq.heappush(heap, merge)
    return heap[0]

def assign_codes(node, cur_code = "", codes = {}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = cur_code
    
    assign_codes(node.left, cur_code + "0", codes)
    assign_codes(node.right, cur_code + "1", codes)

    return codes

ch = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

root = build_huffman_tree(ch, freq)

codes = assign_codes(root)

print("Ký tự và mã Huffman:")
for char in codes:
    print(f"{char}: {codes[char]}")