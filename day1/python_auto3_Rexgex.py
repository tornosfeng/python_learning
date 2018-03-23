import re

pattern1 = "cat"
pattern2 =  "bird"





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




