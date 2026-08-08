class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        lookup = set(wordDict)
        results = []
        def go(index, tmp):
            if index == N:
                results.append("".join(tmp[:]).strip())
                return
            current = ""
            for i in range(index, N):
                current = current + s[i]
                if current in lookup:
                    tmp.append(current+" ")
                    go(i + 1, tmp)
                    tmp.pop()
        go(0, [])
        return results         
