class FreqStack:

    def __init__(self):
        self.sl1 = SortedList() #f, v
        self.sl2 = SortedList() #v, f
        self.mp = defaultdict(list)
        self.x = 0
        

    def push(self, val: int) -> None:
        i = self.sl2.bisect_left((val, float("-inf"), float("-inf")))
        self.x+=1
        self.mp[val].append(self.x)
        if i < len(self.sl2) and self.sl2[i][0] == val:
            _, f, t = self.sl2.pop(i)
            j = self.sl1.bisect_left((f, t, val))
            f, _, _ = self.sl1.pop(j)
            self.sl1.add((f+1, self.x, val))
            self.sl2.add((val, f+1, self.x))
        else:

            self.sl1.add((1, self.x, val))
            self.sl2.add((val, 1, self.x)) 


    def pop(self) -> int:
        # print(self.sl1, "\n", self.sl2)
        if len(self.sl1):
            f, t, v = self.sl1.pop(len(self.sl1)-1)
            i = self.sl2.bisect_left((v, f, t))
            _, _, _ = self.sl2.pop(i)
            self.mp[v].pop()
            if f - 1 > 0:
                pt = self.mp[v][-1]
                self.sl2.add((v, f-1, pt))
                self.sl1.add((f-1, pt, v))
            return v
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()