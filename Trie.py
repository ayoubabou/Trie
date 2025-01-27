class TrieNode:
    def __init__(self,letter=None):
        self.letter = letter
        self.children = []
        self.endOfWord = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        currentNode = self.root
        for i in range(len(word)):
            for child in currentNode.children:
                if child.letter==word[i]:
                    currentNode = child
                    break
            else:
                newNode = TrieNode(word[i])
                currentNode.children.append(newNode)
                currentNode = newNode
        currentNode.endOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        i = 0
        while i<len(word):
            for child in currentNode.children:
                if child.letter==word[i]:
                    currentNode = child
                    break
            else:
                return False
            i+=1
        return currentNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        i = 0
        while i<len(prefix):
            for child in currentNode.children:
                if child.letter==prefix[i]:
                    currentNode = child
                    break
            else:
                return False
            i+=1
        return True

