
l=[10,20,30,40,50,55,60]
d=[i/10 for i in l  ]
print(d)

x=[i for i in range(10) if i%2==0 ]
print(x)

s='aLphaBEts'
count1=0
count=[i for i in s if i in ('a','e','i','o','u','A','E','I','O','U')]
print(len(count))
new= [i.lower() if i.isupper() else i.upper() for i in s]
print(new)

"""Input a string from user, create a list of only those words whose length is more than 5
characters. """
s="dattatri hi shalivan godam wel"
spl=[i for i in s.split() if len(i)>=5]
print(spl)

w="words"
word=[w[j] for i in range(len(w)) for j in range(i)]
print(word)