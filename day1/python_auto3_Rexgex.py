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







