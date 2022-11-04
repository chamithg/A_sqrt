class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        midPoint = x//2
        
        if midPoint * midPoint == x:
            return midPoint
        
        
        while midPoint * midPoint != x:
            print(midPoint)
            
            if midPoint* midPoint < x and midPoint +1 * midPoint+1 > x:
                return midPoint
            
            if midPoint* midPoint < x:
                midPoint = x- midPoint //2
            else:
                midPoint = midPoint //2
            
            
        
        
        

obj = Solution()

print(obj.mySqrt(2147395599))