class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        k = 0
        i = 0
        new_string = ''
        length = len(strs[0])
        
        if length == 0:
            return new_string
        
        while k <= length:
            print(new_string)
            for i in range(len(strs)-1):
                if strs[i][k:k+1] != strs[i+1][k:k+1]:
                    return new_string
            
            new_string += strs[i][k:k+1]
            
            k += 1
            
        return new_string
            
        
        