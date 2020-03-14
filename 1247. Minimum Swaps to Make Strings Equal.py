class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if not s1:
            return 0
        
        n = len(s1)
        case1 = 0; case2 = 0
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    case1 += 1
                else:
                    case2 += 1
        if (case1 + case2) % 2 == 1:
            return -1
        else:
            return case1 // 2 + case2 // 2 + (case1 % 2) * 2
