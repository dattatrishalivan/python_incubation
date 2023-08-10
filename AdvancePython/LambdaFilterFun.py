"""Use filter function to filter a list of numbers and strings such that the result contains only
numbers. (Hint : Use isinstance method) """

l=[2,3,'da','ad',5,6,'tr']
lst=list(filter(lambda x: isinstance(x,int),l))
print(lst)