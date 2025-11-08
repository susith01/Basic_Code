class Solution:
    def evenlyDivides(self, n):
        count = 0              
        for i in str(n):      
          d = int(i)           
          if d != 0:          
            if n % d == 0:
             count += 1   
        return count

obj=Solution()
n=120
result=obj.evenlyDivides(n)
print(result)   