# Key-Value 자료 쌍으로 이루어진 자료형
# Key: 자료를 찾기 위한 기준값(리스트의 인덱스)
# Value: 저장하고자 하는 자료(리스트의 값)
# key는 중복이 허용되지 않으나, value는 중복이 허용된다. 
# 입력 순서가 보장된다(Python3.6부터).

# dictionary의 생성
x = {} # 빈 딕셔너리 생성1(이로 인해 set은 이렇게 쓸 수 없음)
print(f'x = {x}')
x = dict() # 빈 딕셔너리 생성2
print(f'x = {x}')

# 초기화1
x = {2: 10, 3: 40, 6: 100} # key: value 쌍으로 자료 입력
print(f'x = {x}')

# 초기화2
x = dict([(2, 10), (3, 40), (6, 100)]) # (key, value) 쌍으로 자료 입력(튜플로, 그리고 리스트로 묶어줌/리스트 자료형 안에 튜플이 있음)
print(f'x = {x}')

# 초기화3
x = dict(key1=10, key2=40, key3=100) # key가 문자열일 때만 가능
print(f'x = {x}')

# 딕셔너리 요소에 접근(key를 이용)
x = {1: 20, 2: 30, 'key1':40, 'key2':30}
print(f'x = {x}')
print(f'x[1] = {x[1]}') # 리스트의 인덱싱처럼 키에 접근
print(f'x["key1"] = {x["key1"]}') # 리스트의 인덱싱처럼 키에 접근

# 딕셔너리 요소 추가, 수정, 제거
x = {1: 10, 2: 20, 3: 30, 4: 40}
print(f'x = {x}')
x[5] = 50 # 리스트의 인덱싱처럼 자료 추가 가능
print(f'x = {x}')
x[5] = 15
print(f'x = {x}') # 키는 중복이 허용되지 않고, 기존 값을 수정하게 됨(value는 중복 가능)

del x[5]
print(f'x = {x}')

# 그 외 기능들
x = {1: 10, 2: 20, 3: 30, 4: 40}
print(f'x.keys() = {x.keys()}') # 키만 출력
print(f'x.values() = {x.values()}') # 값만 출력

y = len(x) # 자료의 개수
print(f'y = {y}')

x.clear() # 비움(리스트, 집합에도 있음)
print(f'x = {x}')