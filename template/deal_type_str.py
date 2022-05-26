""" 
deal of <class 'str'>
lower alpha : 'abcdefghijklmnopqrstuvwxyz'
upper aphaa : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""

# 空文字列の作成
string = ""
string = str()

# 判定系
string.islower() # type : <class'bool'>
string.isupper() # type : <class'bool'>
string.isdigit() # type : <class'bool'>
# から文字列はいづれもFalseを返す

# 大文字小文字に変換
string.lower()
string.upper()
string.capitalize()

# エスケープシーケンスの利用
string = "It\'s small world!"

# 文字列内の検索
tar in string # type : <class 'bool'>
count = string.count(tar [, start, end])
idx = string.find(tar [, start, end])
idx = string.rfind(tar [, start, end])

# 文字列内の検索（全てを調べてリストとしてstart位置のidxを返す）
import re
s = 'I am Sam'
[m.start() for m in re.finditer('am', s)] # [2, 6]
# 該当箇所がなければ空のリストを返す

# 文字列の置換
s.replace('I', 'We') # 'We am Sam'

# format
"{}".format(arg)
"{a}, {b}".format_map({'a':"hello", 'b':"world"}) # 'hello, world'

# 型の変換
samp = 'abc def'
list(samp) # ['a', 'b', 'c', ' ', 'd', 'e', 'f']
samp.split(sep=None) # ['abc', 'def']

# Unicode 上の扱い
chr(97) # 'a'
chr(49) # '1'
ord('a') # 97
ord('1') # 49



