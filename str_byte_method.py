#Byte object
#it is a built intype for manupulating binary data,it immutable sequence
#each element in byte object is small intger range 0 to 255
b = b'folk,kar'
print(b)
print(type(b))

b1 = b'dan\xbader'
print(b1)
print(b1[2])
# b2 = bytes('joker')# error need to pass encode
b2 = bytes('joker','utf8')
print(b2)
print(bytes(8))

b3 = b'abcd'
print(b'cd' in b3)
b4 = b'efgh'
b5 = b3+b4
print(b5)
print(len(b5))
print(min(b5))
print(max(b5))#returns ascii value of the a

#bytearray()
#it is another sequence for binary objct
#it is mutable
ba = bytearray('foo bar baz','utf8')
print(ba)
print(len(ba))
ba[3]=30
print(ba)
