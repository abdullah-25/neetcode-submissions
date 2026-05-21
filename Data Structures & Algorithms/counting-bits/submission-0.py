class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            one_count = str(bin(i)[2:]).count('1')
            res.append(one_count)
        return res
