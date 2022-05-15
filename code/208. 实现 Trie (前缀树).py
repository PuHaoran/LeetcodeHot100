"""
208. 实现 Trie (前缀树)
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
"""
""" 题解
字典树(前缀树)。使用二维数组构造一个存储和查找字符串的数据结构，arr[x][y]的值代表当前节点x(索引)对应的26的字母之一y对应的节点(索引)，cnt[N]存储当前字符串出现次数。
"""


class Trie:

    def __init__(self):
        N = 100010
        self.idx = 0
        self.arr = [[0]*26 for _ in range(N)]
        self.cnt = [0]*N

    def insert(self, word: str) -> None:
        p = 0
        for c in word:
            u = ord(c)-ord('a')
            if not self.arr[p][u]:
                self.idx += 1
                self.arr[p][u] = self.idx
            p = self.arr[p][u]
        self.cnt[p] += 1

    def search(self, word: str) -> bool:
        p = 0
        for c in word:
            u = ord(c)-ord('a')
            if not self.arr[p][u]:
                return False
            p = self.arr[p][u]
        if not self.cnt[p]:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        p = 0
        for c in prefix:
            u = ord(c)-ord('a')
            if not self.arr[p][u]:
                return False
            p = self.arr[p][u]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
