class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None
class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_dict=WordDictionary()
        res=[]
        rows=len(board)
        cols=len(board[0])
        for word in words:
            word_dict.addWord(word)
        def dfs(r,c,node):
            if ( r<0 or r>=rows or c<0 or c >=cols or board[r][c]not in node.children):
                return 
            char=board[r][c]
            next_node=node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word=(None)
            board[r][c]="#"
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            board[r][c]=char

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,word_dict.root)
        return res
        