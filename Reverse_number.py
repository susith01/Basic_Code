class Number:
    def __init__(self,num):
        self.num=num
    def reverse(self):
        rev=int(str(self.num)[::-1])
        return rev 

n=Number(123) 
print(n.reverse())  