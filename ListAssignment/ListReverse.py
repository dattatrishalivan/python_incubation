"""1. WAF: reverse_list() that takes a list as argument and reverses the elements of the list in
place (use indexing operations, not any function or slicing)
Logic: if l = [1,2,3,4,5] ; result = [5,4,3,2,1]
1 2 3 4 5 # string
0 1 2 3 4 # indexes
start index = 0, end index = 4; swap the elements at index 0,4
[5,2,3,4,1]
start index = 1, end index = 3; swap the elements at index 1,3
[5,4,3,2,1]
Index start index 2 is not less than end index 2. so no need to go forward"""
l=[1,2,3,4,5]
def reverse_list(l):
    l1=len(l)-1
    for i in range(0,l1-1):
        if i<=l1-i :
            #print(i,l1-i)
            l[i],l[l1-i]=l[l1-i],l[i]
        else:
            break
    print(l)
reverse_list(l)
