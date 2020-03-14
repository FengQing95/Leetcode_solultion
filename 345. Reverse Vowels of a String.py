class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if not s:
            return s
        myList = list(s)
        left = 0
        right = len(myList) - 1

        while left <= right:
            if myList[left] not in vowels:
                left += 1
            elif myList[right] not in vowels:
                right -= 1
            else:
                myList[left], myList[right] = myList[right], myList[left]
                left += 1; right -= 1
        
        res = ""
        for i in myList:
            res += i
        return res
