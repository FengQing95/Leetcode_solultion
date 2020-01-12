class Solution:
    def isAlienSorted(self, words, order):
        if len(words) <= 1:
            return True
        else:
            table = {}
            res = True
            for i in range(26):
                table[order[i]] = i
            
            for i in range(len(words) - 1):
                prev = words[i]
                cur = words[i + 1]
                ptr = 0
                while ptr < len(prev) and ptr < len(cur):
                    if table[prev[ptr]] > table[cur[ptr]]:
                        return False
                    elif table[prev[ptr]] == table[cur[ptr]]:
                        ptr += 1
                    else:
                        break
                if len(prev) > len(cur) and ptr == len(cur):
                    return False
            return True
