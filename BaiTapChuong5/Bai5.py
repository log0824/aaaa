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
            if node.is_end_of_word:
                return False
        node.is_end_of_word = True

        if node.children:
            return False
        return True

def check_good_or_bad(strings):
    trie = Trie()
    for string in strings:
        if not trie.insert(string):
            return "BAD"
        
    return "GOOD"
strings = ["ab", "bc", "cd"]
result = check_good_or_bad(strings)
print(result)
