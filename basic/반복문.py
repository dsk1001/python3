# while 문
from fcntl import DN_DELETE


num = 1
while num <= 100: # num가 100 이하일 때 까지 반복
    print(num)
    num = num + 1 # 한 번 반복 될 때마다 num를 1씩 증가

# for 문
list = ['one', 'two', 'three']
for i in list :
    print(i) ## list 안의 항목을 모두 출력

list2 = [(1,2), (3,4), (5,6)]
for (first, last) in list2 :
    print(first+last) # 각 튜플의 first+last 한 값을 출력

# 연습문제
"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 
합격인지 불합격인지 결과를 보여 주시오.
"""
