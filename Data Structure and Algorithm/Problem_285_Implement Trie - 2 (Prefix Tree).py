"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
    int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the prefix prefix.
    void erase(String word) Removes one instance of the string word from the trie. If the string word does not exist in the trie, do nothing.
    
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count_prefix = 0       #How Many ending with these Prefixes
        self.end_count  = 0         #How many these words

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # INSERT
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count_prefix += 1          # Every new node / char is a prefix
        node.end_count += 1                 # How many ending with same words

    # SEARCH
    def countWordsEqualTo(self, word: str) :
        node = self.root

        for char in word:
            if char not in node.children :
                return 0
            node = node.children[char]
        return node.end_count
            

    # START-WITH
    def countWordsStartingWith(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count_prefix



    def erase(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
            node.count_prefix -= 1
        
        node.end_count -= 1



obj = Trie()
word = "Hello"
prefix = "Hell"
obj.insert(word)
param_2 = obj.countWordsEqualTo(word)
param_3 = obj.countWordsStartingWith(prefix)
print(param_2)
print(param_3)

obj.erase(word)
print(obj.countWordsEqualTo(word))

# Output :
#         1
#         1
#         0