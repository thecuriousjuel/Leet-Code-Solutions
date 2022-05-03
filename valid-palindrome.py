class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        w1 = w2 = ''
        
        for i in s:
            if i.isalnum():
                w1 = w1 + i.lower()
                w2 = i.lower() + w2
        
            
        return w1 == w2