class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        return (self.v)
def xyz(a,b):
    return(a+b)

a=int(input())
b=int(input())
sum=xyz(a,b)
if sum < 150:
    raise MyException("Custom Exception Occured")
else:
    print(sum)
