"""
- 리스트는 []로 선언
- 인덱스 번호는 [0,1,2,3,4....]
"""
family = ['mother', 'father', 'brother1', 'brother2', 'sister']

# len() : 리스트의 길이 출력
print(len(family)) # 출력 결과 : 5


# family[n] : family 리스트 내 항목 출력
print('우리 집 대빵은 '+family[0]+'입니다.') # 출력 결과 : 우리 집 대빵은 mother입니다.

# remove() : 리스트 내 항목 제거
family.remove('sister')
print(family) # 출력 결과 : ['mother', 'father', 'brother1', 'brother2']

# append() : 리스트의 끝에 항목 추가
family.append('sister')
print(family) # 출력 결과 : 

# insert() : 리스트 중간에, 원하는 index에 항목 추가
family.insert(3,'dog')
print(family)

# del : 리스트 중간에, 원하는 index 항목 제거
del family[5]
print(family)

# pop() : 원하는 값을 반환하며 리스트에서 제거
사랑하는동생 = family.pop(3)
print(사랑하는동생)
print(family)