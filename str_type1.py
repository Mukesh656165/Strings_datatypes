# ord()  function return ASCII values
print(ord('a'))
print(ord('#'))

# chr() function return integer values

print(chr(97))
print(chr(65))

print(chr(91))

# String Indexing
s = 'Whysoserious'
print(s[-1])
print(s[0])
print(len(s))
print(s[-len(s)]) # It is accessing the 1st element of the string

s = 'foobar'
# print(s[2:])
# print(s[2:len(s)])
# Both produce the same output

s = 'foobar'
print(s[4:])
print(s[:4])
print(s[:4]+s[4:])

# checking memory management

s = 'Joker'
t = s[:]
print(t)
print(id(t))
print(id(s))
print(s is t)

print(s[2:2])
print(s[4:1])

#string slice

s = 'joker'
print(s[-4:-1])
print(s[1:4])
print(s[-4:-1]==s[1:4])

s = 'Jokerr'
print(s[0:6:2])
print(s[3:0:-2])

# Use of f-string

j = 20
k = 30
prod = j*k
print(f'the product of {j} and {k} is {prod}')

# use of triple quotes on
var = 'Why so serius'
print(f'Joker says {var}')
print(f"joker says {var}")
print(f'''joker says {var}''')