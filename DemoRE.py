# DemoRE.py
import re

#함정을 추가
result=re.search("[0-9]*th","  35th")
print(result)
print(result.group())

# result=re.match("[0-9]*th","  35th")
# print(result)
# print(result.group())

result = re.search("apple","this is apple")
print(result.group())
result=re.search("\d{4}","올해는 2023년입니다.")
print(result.group())
result=re.search("\d{4}","우리동네틑 52300")
print(result.group())