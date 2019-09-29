#print a string with quotes
s = 'Joker'
print(s)
print(repr(s))


# To find duplicate value

from collections import Counter

def dup_str(string):
    f_count = Counter(string)
    for k in f_count.keys():
        if f_count.get(k)>1:
            print(k + ","+str(f_count.get(k)))
mystr = 'Jason bbourne'
a = dup_str(mystr)
print(a)

# find out common letter between two strings

user_str1 = input('enter string 1:')
user_str2 = input('enter string 2:')
s1 = set(user_str1)
s2 = set(user_str2)
lst = list(s1 & s2)
print('common letter : {}'.format(lst))