class Trie:
    """
    208.实现 Trie (前缀树) https://leetcode-cn.com/problems/implement-trie-prefix-tree/
    """
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == "__main__":
    sol = Trie()
    sol.insert("test")
    sol.insert("word")
    print(sol.search("test"))
    print(sol.startWith("wo"))
