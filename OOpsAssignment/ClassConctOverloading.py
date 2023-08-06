class Test:
    def __init__(self):
        print("â€œConstructorâ€")
    def __del__(self):
        print("â€œDestructorâ€")

s1 = Test()
s2 = Test ()

class Test:
    def __init__(self):
        print("â€œConstructorâ€")
    def __del__(self):
        print("â€œDestructorâ€")
s1 = Test()
Test()
s2 = Test()
s3 = s1
del(s1)