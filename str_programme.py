# write a programme to reverse a string
#Tech 1-> Using of slice method
s =  'rekoj'
op = s[::-1]
print(op)

# when using slice oprator step size should be a pos or neg number otherwise error
op1= s[::0]
print(op1)
# take input from user
s1 = input('enter a string to reverse :')
ops1= s1[::-1]
print(ops1)

#Tech -2
p = 'mukesh'
r = reversed(p)
print(r)
print(type(r))
for ch in r:
    print(ch,end='')
#Tech - 3
p1 = 'mukesh_kumar'
r1 = reversed(p1)
output = ''.join(r1)
print(output)

#Tech -4
a = 'mukesh'
re = ''
i = len(a)-1
while i >=0:
    re = re+a[i]
    i = i-1
print(re)
Tech - 5
text = 'Mukesh'
l = ''
for i in text:
    l = i+l
print(l)

