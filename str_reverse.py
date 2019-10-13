
# Programme to reverse the order of words present in the strings
s = 'why so serious'
'''make the string to a list'''
r = s.split()
print(r)
'''reverse the list using slice oprator'''
l = r[::-1]
print(l)
'''make the list as a string using join method'''
op = ' '.join(l)
print(op)

# programme to reverse each content in the given strings
s1 = 'The Dark Knight '

'''make the string as list using split method'''
a1= s1.split()
'''Take aa empty list to appnd the reverse data '''
l1 = []
'''using for loop to read and append charcter by charecter'''
for ch in a1:
    l1.append(ch[::-1])
print(l1)
'''make the list as string by using join method'''
op1 = ' '.join(l1)
print(op1)

# a programme to reverse internal content of every second word present in the given string
s2 = 'The Dark Knight Rise By The Joker'
'''1st make the string as list'''
l2 = s2.split()
print(l2)
'''Declare a empty list to reverse the list and append the list token inside the
empty list'''
a2 = []
'''i value intially zero or start with zero'''
i = 0
'''every 2nd letter holds the odd number so take while loop
and make if even then take as it and if odd then reverse it'''
while i <len(l2):
    if i %2 ==0:
        a2.append(l2[i])
    else:
        a2.append(l2[i][::-1])
    i = i +1
print(a2)
'''now make a2 as string using join method'''
op3 = ' '.join(a2)
print(op3)

# in for loop
s3 = 'The Hero Is Comming Again'
'''make the string into a list using split method'''
a5 = s3.split()
'''chk if it is list'''
print(a5)
'''now declare a empty list which is going to hold the reverse list'''
g = []
'''now take for loop bcz every 2nd item holds odd number
so if it is even then no need to change only odd we should reverse'''
for i in range(len(a5)):
    if i % 2 ==0:
        g.append(a5[i])
    else:
        g.append(a5[i][::-1])
print(g)
'''now change the List(g) into a string using join method'''
op5 = ' '.join(g)
print(op5)
