class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        else:
            res = []
            counts = {}
            for word in strs:
                target = "".join(sorted(word))
                if target not in counts.keys():
                    counts[target] = [word]
                else:
                    counts[target].append(word)

            for count in counts.keys():
                res.append(counts[count])
            return res
