"""Create a class SelfManaged such that it keeps track of the number of objects currently alive.
Create a class method get_current_count(), that gives the number of objects currently alive in
memory.
[Hint: use a class attribute to keep count of number of objects and use __init__ and
 __del__ methods to update the value of count]"""
class SelfManaged:
    count=0
    def __init__(self):
        SelfManaged.count+=1
    def __del__(self):
        SelfManaged.count-=1
    def get_current_count(self):
        print(self.count)
s=SelfManaged()
s1=SelfManaged()
s2=SelfManaged()
del(s1)
s3=SelfManaged()
s.get_current_count()