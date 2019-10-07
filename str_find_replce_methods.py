#count()
# It will return number occurance in the string
print('Jooker_IS_one_of_the_most_dangeriuos_Guy'.count('o'))
# Using Start and end parameter with count
s ='foo goo soo doo'
print(len(s))
print(s.count('o',0,10))
#endswith()
#it returns true if ends with specified charecter is present
s = 'Joker'
print(s.endswith('ker'))
print(s.endswith('k',0,3))#it will search from index 0 to 3 k is present or not

#find()
#it will return the lowest index of substring when found
#if the string is not available it will return -1
print('raz baz jazz amaze audi killer'.find('jazz'))
print('baz raz baz raz raz jazz dhami'.find('raz'))
print('dhami joker arya '.find('stark'))
# Using of star and end
print('baz raz baz raz raz jazz dhami'.find('raz',6,15))
#index()
#it is identical of find method here if sub string is not found then it will raises exception
print('raz baz jazz amaze audi killer'.index('jazz'))
print('baz raz baz raz raz jazz dhami'.index('raz'))
print('dhami joker arya '.index('stark'))
#ValueError: substring not found

#rfind()
#it will return the highst index of the given substring
# if the substring is not found it will return -1
print('foo bar baz raz jaz foo baz jazz'.rfind('foo'))
print('dhami joker arya '.rfind('stark'))
print('foo bar baz raz jaz foo baz jazz'.rfind('foo',0,10))

#rindex()
# this method is identical to rfind except if index not found it will raise an excep[tion
print('foo bar baz raz jaz foo baz jazz'.rindex('foo'))
print('dhami joker arya '.rindex('stark'))

#startwith()
# it will return true if the string is startwith the specified strings
print('joooker'.startswith('jooo'))
print('joker'.startswith('baz'))
print('joooker'.startswith('ker',4))
print('joooker'.startswith('ker',4,3))




