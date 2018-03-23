import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.search('sadifoqiwe0irjopimxcvz;lvjopiqeuopiweuiodsmfgoqwem')
mo = vowelRegex.findall('sadifoqiwe0irjopimxcvz;lvjopiqeuopiweuiodsmfgoqwem')
print(mo1.group())
print(mo)

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
'''利用search匹配的是第一个满足条件的组合'''

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

mo3 = heroRegex.findall('Tina Fey and Batman')
print(mo3)
'''利用findall匹配的是所有满足条件的组合，返回值为list'''

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




