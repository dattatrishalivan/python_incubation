s = "epam systems india pvt limited"
def frequency_of_words(s):
    s1 = s.split()
    d = {}
    for i in s1:
        le = len(i)
        d[i] = le
    print(d)
frequency_of_words(s)