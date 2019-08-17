class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.last = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        self.words = []

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        
        for a in word:
            if not node.children.get(a):
                node.insert(a)

            node = node.children[a]

        node.last = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        not_found = False
        temp_word = '' 

        for a in prefix:
            if not node.children.get(a): 
                not_found = True
                break
  
            temp_word += a 
            node = node.children[a] 

        if not_found: 
            return False
        elif node.last and not node.children: 
            return False

        self.words = []
        self.suffixes(node, temp_word)

        for s in self.words: 
            print(s) 
            
        return True


    def suffixes(self, node, word):
        if node.last:
            self.words.append(word)

        for a, n in node.children.items():
            self.suffixes(n, word + a)



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
    else:
        print('')
interact(f,prefix='');