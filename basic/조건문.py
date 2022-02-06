# if 문
"""
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
elif 조건문:
    수행할 문장a
    수행할 문장b
else:
    수행할 문장A
    수행할 문장B
    ...
"""

# 비교 연산자
"""
x < y
x <= y
x > y
x >= y
x == y
x != y

x and y
x or y
not x

x in 리스트
x in 튜플
x in 문자열
"""

# 예제 1
snack = 1000
money = 500
card = True
if money >= 1000:
    print("그냥 가자")
else:
    print("과자를 사가자")

if money >= 1000 or card:
    print("카드로 과자를 사가자")
else:
    print("현금도 없고 카드도 없다... 그냥 가자")

pocket = ['recipt', 'mobilephone', 'card', 'money']
if 'money' in pocket:
    print("과자를 사가자")
else:
    print("그냥 가자")


if 'money' in pocket:
    print("과자를 사가자")
elif 'card' in pocket:
    print("과자를 사가자")
else:
    print("그냥 가자")