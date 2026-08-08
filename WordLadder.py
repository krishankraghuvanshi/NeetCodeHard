class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:

        from collections import defaultdict

        n = len(wordList)

        graph = defaultdict(lambda : [])

        def f(x, y):
            cnt = 0
            for a, b in zip(x, y):
                if a != b:
                    cnt += 1
                if cnt > 1:
                    return False
            return cnt == 1           

        for i in range(n):
            for j in range(i+1, n): 
                if f(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        if start not in graph:
            for nei in wordList:
                if f(start, nei):
                    graph[start].append(nei)

        q = deque()
        q.append((0, start)) 
        best = defaultdict(lambda : float("inf"))
        best[start] = 0
        visited = {start}

        while q:
            x, u = q.popleft()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    best[v] = x+1
                    q.append((x+1, v))
        if best[end]==float("inf"):
            return 0
        return best[end]+1    

