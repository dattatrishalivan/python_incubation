""" WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
common words in both the sentences.
[Hint: store all the in a set. Read the documentation for set.]"""

s='you are welcome to epam'
s1='you are in epam'
s=s.split()
s1=s1.split()
set1=set()
se2=[]
def uncommon_words(s,s1):
    for i in range(len(s)):
        for j in range(len(s1)):
            if s[i]==s1[j]:
                set1.add(s[i])
    print(set1)
uncommon_words(s,s1)