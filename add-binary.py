class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def binary_to_decimal(n):
            j = 1
            s = 0
            for i in range(len(n)):
                s += int(n[i]) * 2 ** (len(n) - j)
                j += 1
                
            return s
            
        def decimal_to_binary(n):
            if n == 0:
                return '0'
            
            s = ''
            while n > 0:
                d = n % 2
                s += str(d)
                n //= 2
                
            return s[::-1]
        
        
        s = binary_to_decimal(a) + binary_to_decimal(b)
        # print(s)
        # print(decimal_to_binary(s))
        
        return decimal_to_binary(s)