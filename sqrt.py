class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        start = 0
        end = x
        
        
        while start+1<end:
            temp = start+end /2
            
            if temp*temp <x:
                start =temp
            if temp*temp > x:
                end = temp
            if temp*temp == x:return int(temp) 
                
        if end* end ==x:return int(end)
        return int(start+end /2)
    
        
        

obj = Solution()

print(obj.mySqrt(4782))