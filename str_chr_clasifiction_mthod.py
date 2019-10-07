#isalnum ()
#it will returns true if given strings contain alphanumeric
print('abc123'.isalnum())
print('abc@123'.isalnum())# it will return false bcz ofspcl charecter present
print('123'.isalnum()) #True
print(''.isalnum())#empty string also return false

#isalpha()
#it will return true if the whole string is in albhetic otherwise return false
print('AbcDef'.isalpha())
print('ABc@'.isalpha())#false
print('abc12'.isalpha())
#isdigit()
# it will check if string is made in only numeric digits then return true
print('123'.isdigit())
print('123abc'.isdigit())
#isidentifier()
# it will return true if the given string is a valid identifier according to python language definition
print('mukes32'.isidentifier())
print('mukes_32'.isidentifier())#true
print('32_kuk'.isidentifier())#false
print('kuk@32'.isidentifier())
#Note: .isidentifier() will return True for a string that matches the python keyword
#even though it is not a valid identifier
print('and'.isidentifier())
print('is'.isidentifier())
# we can test the string matches a keyword or not in python
from keyword import iskeyword
print(iskeyword('and'))
print(iskeyword('is'))
# if you really want to ensure the string is serve as valid python identifier
# you should check that isidentifier() is true and iskeyword() is false

#islower()
#it will return true if the string contains all charecter in lower case
#and all nonalphabetic charecters are ignore in this method
print('mukesh'.islower())
print('mukesh@123'.islower())
print('Mukesh$12'.islower())#false
#isprintable()
#it will returns true if the string is empty,and if the strings contains alphabetic are printable
#it returns false if the string contains atleast one nonprintable  charecter
#and nonalphabetics are ignored here also
print(''.isprintable())
print('abc123'.isprintable())
print('mks'.isprintable())
print('b\tnm'.isprintable())
#isprintable() it is the only methods return true if the string is empty all others return false
#isspace()
#it returns true if string contains whitespace otherwise returnss false
# Most commonly encounter whitespaces are tab \t and newline \n
print(' \t \n'.isspace())
print('  a  '.isspace())
#few ASCII charecters encouted as whitespacees
print('\f\u2005\r'.isspace())
#\f and \r are are the escape sequences for ASCII form feed and carriege
#return charecter u2005 is from unicode escape sequence for  Unicode Four-Per-Em Space.
#istitle()
# it returns true if the string contains the 1st charecter of everyword contain capital
#and remining small
print('Why So Serious'.istitle())
print('why so serious'.istitle())
print('Joker Is @#Tittle'.istitle())#true Non alphabetics ignored in this case
print('Joker Is Awe@$#some'.istitle())# return false
print('Joker Is Awe@#$ Some'.istitle())# true
# isupper()
# it returns true if the string contains upprcase nonaplphabetics will ignored
print('ABC'.isupper())
print('abcD'.isupper())
print('ABC#@#$'.isupper())#true
print('ABC1@#$D'.isupper())