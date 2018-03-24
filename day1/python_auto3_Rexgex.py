import re


'''利用括号分组'''

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())

'''利用 | 管道符号匹配多个分组'''

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
mo3 = heroRegex.findall('Tina Fey and Batman')
print(mo3)


'''利用 * 号匹配零次或多次'''
batRegex  = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventrue of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventure of Batwowowoman')
print(mo3.group())

'''利用 + 号匹配一次或多次'''
batRegex  = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1 == None)
mo2 = batRegex.search('The Adventrue of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventure of Batwowowoman')
print(mo3.group())

'''利用{}括号匹配制定次数'''

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('HaHaHa')
print(mo.group())

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())  #默认贪心匹配，选择尽可能长的字符串。

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())  #此时可以用问号？声明非贪心匹配。


'''利用search匹配的是第一个满足条件的组合'''
'''利用findall匹配的是所有满足条件的组合，返回值为list'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work:212-555-0000')
print(mo.group())
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work:212-555-0000')
print(mo1)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work:212-555-0000')
print(mo2)

'''字符分类可以缩短正则表达式，如\d \D  \w  \W  \s  \S   [0-5]'''
xmasRegex = re.compile(r'\d+\s\w+')   #匹配至少一位数字+空白字符+至少一位数字，字母或下划线
mo1 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo1)


'''采用[ ]方括号可以定义字符分类，方括号内，普通的正则表达式符号不会被解释，因此不需要进行转义'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('sadifoqiwe0irjopimxcvz;lvjopiqeuopiweuiodsmfgoqwem')
print(mo)
'''采用[ ]方括号的左括号后加上一个插入字符  ^  , 可以得到非字符类，用来匹配不在这个字符类中的所有字符'''
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

'''正则表达式起始使用  ^  插入符号，表示匹配必须发生在被查找文件的开始处'''
'''正则表达式末尾使用  $  美元符号，表示匹配必须满足以正则表达式的模式结束'''

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world'))
print(beginsWithHello.search('He said Hello') == None)

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your numver is forty two') == None)

wholeStringIsNum = re.compile(r'^\d+$')  #表示从开始到结束都是数字
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)

'''正则表达式中，   .   句点表示通配符，匹配除了换行以外的所有单个字符,如果要直接匹配真正的句点，需要用\转义'''
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

'''用 .* 匹配所有字符  (默认使用贪心模式，匹配尽可能多的文本)'''

nameRegex = re.compile(r'First Name:(.*)Last Name:(.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())
greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())