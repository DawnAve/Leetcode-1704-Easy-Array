class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Vowels
        length = len(s)//2
        first = s[:length]
        second = s[length:]
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count  = 0
        for i in first:
            if i in v:
                count +=1
        for i in second:
            if i in v:
                count -=1
        return not count
