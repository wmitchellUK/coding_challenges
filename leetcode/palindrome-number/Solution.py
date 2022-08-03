class Solution:
    def isPalindrome(self, x: int) -> bool:
        paramStr = str(x)
        reversedStr = ''.join(reversed(paramStr))
        print(paramStr)
        if reversedStr == paramStr:
            return True
        else:
            return False
        
# Tips 
# str(x) - gives a string
# reversed() returns a list
# ''.join takes a list and joins with the separator
