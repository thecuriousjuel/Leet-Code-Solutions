class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = ' ' + s
        
        w = ''
        for i in s[::-1]:
            if i == ' ':
                if w:
                    return len(w)
                continue
            w = i + w
            