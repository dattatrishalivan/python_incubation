# WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
#Update the above program to also print the sum of numbers.
def input_numbers():
    l=[]
    sum=0
    print("input 10 numbers : ")
    for i in range(10):
        n=int(input())
        l.append(n)
        sum=sum+n
    print(l)
    print("Sum : ", sum)
input_numbers()