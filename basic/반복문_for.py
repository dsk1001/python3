# for 문
list = ['one', 'two', 'three']
for i in list :
    print(i) ## list 안의 항목을 모두 출력

list2 = [(1,2), (3,4), (5,6)]
for (first, last) in list2:
    print(first+last) # 각 튜플의 first+last 한 값을 출력

# 예제 - 합격, 불합격
"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 
합격인지 불합격인지 결과를 보여 주시오.
"""
scores = [90, 25, 67, 45, 80]
number = 0 # 몇 번째 학생인지 지정
for score in scores:
    number = number + 1
    if score >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# continue
number1 = 0
for score in scores:
    number1 = number1 + 1
    if score >= 60:
        print("%d번 학생은 합격입니다." % number1)
    else:
        continue # 불합격인 학생이 있을 시 다시 조건문 처음으로 돌아간다.

# range()
a = range(10) # 0부터 10 미만인 숫자를 포함
print(a)
b = range(0,10) # 0부터 10 미만인 숫자를 포함
print(b)

# range()를 이용하여 1부터 10까지 더하기
add = 0
for i in range(1, 11):
    add = add + i
print(add)

# range()를 이용하여 위의 합격, 불합격 예제 작성
number2 = 0
for number2 in range(len(scores)): # range(5), 0 1 2 3 4
    if scores[number2] >= 60:
        print("%d번 학생은 합격입니다." % (number2+1))
    else:
        continue

# for와 range를 이용한 구구단
for i in range(2,10): # 2,3,4,5,6,7,8,9
    print("%d단" %i)
    for j in range(1,10):
        print(i*j, end=" ") # end : 그 줄에 계속 출력
    print('\n')

# 트리 만들기
a = int(input("몇 단 트리로 만드시겠습니까? 입력 해주세요 : "))
range1 = range(1,a+1)
for a in range1:
    print(" "*(len(range1)-a)+"⭐️"*a)
print('\n')

# 다이아몬드 만들기
b = int(input("너비가 몇인 다이아몬드를 만드시겠습니까? 입력 해주세요 : "))
range2 = range(1,b+1)
for b in range2:
    print(" "*(len(range2)-b)+"⭐️"*b)
for b in range2:
    print(" "*b+"⭐️"*(len(range2)-b))

# 모래시계 만들기
c = int(input("너비가 몇인 모래시계를 만드시겠습니까? 입력 해주세요 : "))
range3 = range(1,c+1)
for c in range3:
    print(" "*c+"⭐️"*(len(range3)-c+1))
for c in range3:
    if c == 1:
        continue
    else:
        print(" "*(len(range3)-c+1)+"⭐️"*c)