# 문자열 만드는 방법
# 1. 작은 따옴표 (') 이용
'dsk'
# 2. 큰 따옴표 (") 이용
"2022"
# 3. 작은 따옴표 3개(''') 이용
''' 문자열 만들기'''
# 4. 큰 따옴표 3개(""") 이용
""" 문자열 만들기 """

"""=========================================="""

# 이스케이프 코드
"""
\\ : 문자열 내부에서 역슬래시 표현
\' : 문자열 내부에서 작은 따옴표 (') 표현
\" : 문자열 내부에서 큰 따옴표 (") 표현
\n : 문자열 내부에서 개행 (줄바꿈)
\t : 문자열에서 간격 주기 (탭)
"""
# 예제
print('1. 이스케이프 코드 \\ 역슬래시 예제')
s1 = "역슬래시는 \\ 이렇게 "
print(s1)

print('\n2. 이스케이프 코드 \' 작은따옴표 예제')
s2 = 'dsk\'s python example'
print(s2)

print('\n3. 이스케이프 코드 \" 큰따옴표 예제')
s3 = "I don't know. \"python string\" abcdef"
print(s3)

print('\n4. 이스케이프 코드 \\n 개행 예제')
s4 = "딸기\n포도\n사과\n"
print(s4)

print('\n5. 이스케이프 코드 \\t 탭 예제')
s5 = "A\tB\t\tC"
print(s5)

"""=========================================="""

# 문자열 인덱싱
"""
각 문자열에는 고유한 인덱스 번호가 존재한다.
 a  b  c  d -> 글자수를 n개라고 하였을 때,
 0  1  2  3 -> 0 ~ n-1
-4 -3 -2 -1 -> -n ~ -1
"""
# 예제
word = "abcd"
print(f"word : {word}")
print(f"word[0] : {word[0]}") # 출력 결과 : a
print(f"word[1] : {word[1]}") # 출력 결과 : b
print(f"word[2] : {word[2]}") # 출력 결과 : c
print(f"word[3] : {word[3]}") # 출력 결과 : d
print(f"word[-1] : {word[-1]}") # 출력 결과 : d
print(f"word[-2] : {word[-2]}") # 출력 결과 : c
print(f"word[-3] : {word[-3]}") # 출력 결과 : b
print(f"word[-4] : {word[-4]}") # 출력 결과 : a
print("\n")

"""=========================================="""

# 문자열 슬라이싱
"""
문자열의 앞, 뒤, 특정 부분을 잘라서 추출할 수 있다.
[:] : 전체 출력
[0:n], [:n] : 처음부터 n-1까지 출력
[n:n+1] : n부터 n-1까지 출력이므로 n 하나만 출력
[n:n+2] : n부터 n+1까지 출력
[n:] : n부터 끝까지 출력
[-n:] : -n부터 끝까지 출력
[-n:-n+1] : -n만 출력
[:-n] : 처음부터 -n-1까지 출력
앞 index부터 끝 index-1까지 출력한다고 생각하면 된다.
"""
# 예제
word2 = "abcd"
print(f"word : {word2}")
print(f"word[:] : {word2[:]}") # 출력 결과 : abcd
print(f"word[:1] : {word2[:1]}") # 출력 결과 : a
print(f"word[0:1] : {word2[0:1]}") # 출력 결과 : a
print(f"word[1:2] : {word2[1:2]}") # 출력 결과 : b
print(f"word[-1:] : {word2[-1:]}") # 출력 결과 : d
print(f"word[-3:-2] : {word2[-3:-2]}") # 출력 결과 : b
print(f"word[-2:] : {word2[-2:]}") # 출력 결과 : cd
print(f"word[:-4] : {word2[:-4]}") # 출력 결과 :
print(f"word[:-3] : {word2[:-3]}") # 출력 결과 : a

name = "doseungkyong"
print(f"성 : {name[:2]}") # 출력 결과 : do
print(f"이름 : {name[2:]}") # 출력 결과 : seungkyong

"""=========================================="""

# 문자열 더하기
word3 = "water" + "melon"
print(word3) # 출력 결과 : watermelon
word4 = "straw" + '\t' + "berry"
print(word4) # 출력 결과 : straw    berry

# 문자열 곱하기
epichigh = "Love "
print(epichigh*3) # 출력 결과 : Love Love Love

"""=========================================="""

# 문자열 길이 구하기
sentence = "Hello, my name is dsk"
print(len(sentence)) # 출력 결과 : 21