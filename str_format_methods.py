# Methods in this group can modify and enhance the string
#center() meth
print('Joker'.center(10))
s = 'Mukesh'
print(s.center(10))
print(len(s))
# center() using fill arguement
print('stark'.center(20,'-'))
print(len('stark'.center(20,'-')))
# if string is already as long as width it will remain unchanged
print('arya'.center(2))

#expandtabs()
print('arya'.expandtabs())
print('arya\tmk'.expandtabs())
print('arya\tjohn_snow\tjaimie'.expandtabs(4))
print('arya\tjohn\tjamie')
print('hello\taa\tgb'.expandtabs(tabsize=4))

#ljust()
print('stark'.ljust(10))
print('stark'.ljust(10,'-'))# it will justify left side and add on rightside of the string

#lstrip()
# it removed any whitespace removed from the left end
print('    msk    '.lstrip())
print('repmkrnrrrmkkk'.lstrip('rep'))
print('aaabbbcdddbba'.lstrip('ab'))# it will remove the matching charecter in leftside also

# IMP method -->replace()
#it will remove the string and replace by new string
s = 'why_sp_serious'
print(s.replace('p','o'))
s1 = 'jokkkerm'
print(s1.replace('k','l'))#it will replace all k
print(s1.replace('k','l',2))# it will replace the k 2 times in left side OP-jollkerm
# next trick to do
s3 = 'jokkker'
print(s3[:3])
print(s3[3:])
print(s3[:3]+'l'+s3[4:])#OP-joklker replce middle of k

#rjust()
#it returns the vice versa of ljust it will justified left side and padd right side
print('jker'.rjust(10,'-'))

#rstrip()
# it will remove whitespace from rightside
print('$$$$muk$$$$'.rstrip('$'))
#strip()
#it will remove whitespace from left and right side it is combination of both rstrip and lstrip
print('$$$$$$$muk$$$$$'.strip('$'))
#check with white spaces
s4 = '\t\tmukesh\t\t\t'
print(repr(s4))
print(s4)
print(s4.lstrip().rstrip())
print(s4.strip())
s5 = 'www.facebook.com'
print(s5.lstrip('w.').rstrip('.com'))
print(s5.strip('w.com'))

#Zfill()
#padding left side into zero
print('520'.zfill(8))
#string contain leading sign other wise it will giving same op
#print('52'.zfill()) #no op
print('jk'.zfill(10))
print('+42'.zfill(8))#note-it store zero after + sign

#Join() imp
#it converts list to strings
print(','.join(['mk','rk','sk']))
print(list('joker'))
print(':'.join('Bark'))
print('->'.join('joker'))
# print('-'.join(['gk',25,'mk'])) op-error need to provide string data type in list
print('-'.join(['25','gk']))

#partition()
# it will split the strings and returns as tuple
print('mukeshkumar'.partition(','))
print('mukesh.kumar'.partition('.'))
print('mukesh@@kumar'.partition('@@'))#('mukesh', '@@', 'kumar')OP
#if separator not found it will return
print('Mukesh_sing'.partition('@@'))#('Mukesh_sing', '', '')OP

#rsplit()
#devide the string into lists
print('apple grape cake'.rsplit())
print('apple\n\tcake juk\t'.rsplit())
print('egg.chiken.mutton'.rsplit())#op['egg.chiken.mutton']
print('egg.chiken.mutton'.rsplit(sep='.'))
print('jk....bk'.rsplit('....'))#op-['jk', 'bk']
print('jk...bk'.rsplit('.'))#op-['jk', '', '', 'bk']
#split()
print('joker,mk'.split())
print('joker.mk'.split('.'))
#split with maxslpit parameter
print('www.facebook.com'.split('.',maxsplit=1))#op-['www', 'facebook.com']
print('www.facebook.com'.rsplit('.',maxsplit=1))#op-['www.facebook', 'com']

#splitlines()
print('m\nk\j\n'.splitlines())
print('ak\nkn\bn'.splitlines(True))