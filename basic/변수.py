"""
- 파이썬에서 다룰 수 있는 자료형(data type)은 크게 숫자, 문자, 그리고 변수가 있다.
- 변수 이름은 알파벳 대/소문자, 숫자, 언더바, 한글, 한자 등을 사용할 수 있다.
- 대, 소문자를 구별한다.
- 첫 글자를 숫자로 시작할 수 없다. (ex 1number, 1_num 등)
- 공백, 특수문자, 문장부호를 변수 이름으로 사용할 수 없다.
"""

# 변수 - 숫자
print("====== 변수 - 숫자 ======")
pencil = 1000
eraser = 500
# pencil, eraser = 1000, 500 이렇게 동시에 여러 변수를 지정할 수 있다.
price = pencil+eraser

print(pencil+eraser)
# 출력 결과 : 1500
print(price)
# 출력 결과 : 1500

print("가격은 " + str(price) + "원 입니다.")
# price는 숫자이므로 문자열로 변환 해야한다.
# 출력 결과 : 가격은 1500원 입니다.

print("연필의 가격은 " + str(pencil) + "원 입니다. 연필 3자루의 가격은 " + str(pencil*3) + "원 입니다.")
# pencil*3으로 pencil 변수 값에 3을 곱할 수 있다.
# 출력 결과 : 연필의 가격은 1000원 입니다. 연필 3자루의 가격은 3000원 입니다.

print("연필의 가격이 500원 올라 " + str(pencil+500) + "원이 되었습니다.")
# pencil+500으로 pencil 변수 값에 500을 더할 수 있다.
# 출력 결과 : 연필의 가격이 500원 올라 1500원이 되었습니다.

# 가격은 한 번 오르면 떨어지지 않는다. 변수 자체에 500원을 더해보자.
pencil = pencil + 500
print(pencil)
# 출력 결과 : 1500


# 변수 - 문자
print("====== 변수 - 문자 ======")
name = 'dsk'
print(name)
# 출력 결과 : dsk

print("제 이름은 " + name + " 입니다.")
# 출력 결과 : 제 이름은 dsk 입니다.

text = "그는 \"안녕. 내 이름은 James야.\" 라고 말했습니다."
print(text)
# 문자열 안에 따옴표를 쓰고싶다면 \" 로 감싸준다.
# 출력 결과 : 그는 "안녕. 내 이름은 James야." 라고 말했습니다.

epichigh = "Love "
print(epichigh*3)
# 해당 문자열을 여러번 반복하여 출력하고 싶다면 * 연산을 사용한다.
# 출력 결과 : Love Love Love