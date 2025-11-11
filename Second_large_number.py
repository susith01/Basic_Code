class solution:
    def __init__(self,number):
        self.number=number
    def sort_number(self):
        self.number.sort()
        return self.number
a=solution([1,13,2,4,15,12])
result=a.sort_number()
print(result)        