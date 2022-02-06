num1 = 4
num2 = 3

print('4 더하기 3은 '+str(num1+num2))
print('4 빼기 3은 '+str(num1-num2))
print('4 곱하기 3은 '+str(num1*num2))
print('4 나누기 3은 '+str(num1/num2))
print('4 나누기 3의 몫은 '+str(num1//num2))
print('4 나누기 3의 나머지는 '+str(num1%num2))
print('4의 3 제곱은 '+str(num1**num2))

# 연습문제
"""
파일을 다운로드할 때의 평균 속도(average rate)를 r이라 하고, 다운로드하는 데 걸린 시간(time)을 t라고 할 때, 다운로드한 파일의 용량은 rxt로 계산할 수 있습니다.
다운로드 속도가 초당 800kB이고 다운로드하는 데 걸린 시간이 110초라고 할 때, 다운로드한 파일의 크기는 몇 MB일까요? 
단, 1MB=1000kB로 계산합니다.
"""

# 정답
r = 800
t = 110
print(r*t/1000)