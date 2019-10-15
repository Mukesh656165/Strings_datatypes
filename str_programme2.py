# a programme to print characters present in even index or odd index
s = 'python'
'''intilize the 1st i value into 0 for even index'''
i = 0
print('character present in even index:')
while i<len(s):
    '''s[i] it means print each and every value present in s through i index'''
    print(s[i])
    '''then increment i value with 2 print for even index'''
    i = i+2
'''now time to print odd index for this'''
'''intialize the i value into 1 ,it starts with one for print odd index'''
i = 1
print('character present in odd index:')
while i <len(s):
    print(s[i])
    ''''then incrent with 2'''
    i = i+2
# Tech -2
s1 = 'developer'
print('character present in even index :',s1[::2])
'''for print odd index slice start with 1 and step size 2'''
print('character present in odd index:',s[1::2])