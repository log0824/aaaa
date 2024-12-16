class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True
    def longest_common_prefix(self):
        prefix = ""
        node = self.root

        while node:
            if len(node.children) == 1 and not node.is_end_of_word:
                char = next(iter(node.children))
                prefix += char
                node = node.children[char]
            else:
                break
        return prefix
    
s = ["flower", "flow", "flight"]
trie = Trie()

for word in s:
    trie.insert(word)

print("Tiền tố chung dài nhất là:", trie.longest_common_prefix())
    