class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        R, C = len(board), len(board[0])

        root = TrieNode()

        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w  

        res = []  

        visited = [[False] * C for _ in range(R)]  

        def solve(x, y, node):
            if not (0 <= x < R and 0 <= y < C):
                return
            if visited[x][y]:
                return
            c = board[x][y]

            if c not in node.children: return

            nxt = node.children[c] 

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None

            visited[x][y] = True

            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy

                solve(nx, ny, nxt)

            visited[x][y] = False

        for i in range(R):
            for j in range(C):
                solve(i, j, root)
        return res                
