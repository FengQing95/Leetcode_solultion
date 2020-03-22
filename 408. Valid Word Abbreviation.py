class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not abbr:
            return False
        i = j = 0
        while j < len(abbr):
            if i >= len(word) or abbr[j] == "0":
                return False

            cur = abbr[j]
            if cur.isnumeric():
                tem = int(cur)
                count = 1
                while j + count <= len(abbr) and abbr[j:j+count].isnumeric():
                    tem = int(abbr[j:j+count])
                    count += 1
                if i + tem <= len(word):
                    i += tem
                    j += count - 1
                else:
                    return False

            else:
                if word[i] != cur:
                    return False
                else:
                    i += 1
                    j += 1

        if i == len(word) and j == len(abbr):
            return True
        else:
            return False
