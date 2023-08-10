# Decorator
age=int(input("enter your age : "))
def dec(fun):
    def inner_fun(*args):
        print("my name is dattatri")
        fun(age)
        print("I am from hyderabad")
        return age
    return inner_fun
@dec
def outer_fun(age):
    print("my age is", age)
outer_fun(age)