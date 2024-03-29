# 리스트와 비슷한, 여러 개의 자료를 묶는 자료형
# 다른 점은, 튜플은 불변형(immutable)-자료의 추가, 수정, 제거가 불가능-임

# 튜플의 생성
x = tuple() # 빈 튜플 생성
print(f'x = {x}') # x = () 일반 괄호로 표현
x = () # 빈 튜플 생성
print(f'x = {x}')
x = (1, 2, 3) # 여러 값을 괄호로 묶으면 튜플
print(f'x = {x}') 
x = (5,) # 값이 하나만 있는 튜플은 ,를 써줘야 튜플이 된다(괄호 연산자와 혼동됨)
# x = (5)
print(f'x = {x}')
x = 1, 2, 3 # 값이 여러 개일 경우 사실 괄호 생략해도 자동으로 튜플됨.
print(f'x = {x}') 

# 튜플 자료에 접근하기 - 리스트와 같다. 
x = (10, 20, 30, 40, 50, 60)
print(f'x[0] = {x[0]}') # 리스트처럼 0으로 시작하는 인덱스 
print(f'x[-1] = {x[-1]}') # 마지막 자료에 접근 
print(f'x[:3] = {x[:3]}') # 슬라이싱도 리스트와 동일, (단, 튜플을 반환 튜플을 슬라이싱하면 튜플이 된다)

# 튜플은 자료의 추가/수정/삭제가 불가능
x = (10, 20, 30, 40, 50, 60)
# del x[1] # 삭제 불가
# x.append(30) # 추가 안됨

# 이어붙이기 이건 됨
x = x + (70, 80) # 새로운 튜플을 '만들기' 때문에 가능 (추가 !== 만들기)
print(f'x = {x}')

# 튜플에서 제공되는 기능 
# x.sort() # 불변형이므로 정렬 불가능
y = x.count(10) # 접근만 하는 것이므로 가능 
print(f'y = {y}') 
y = x.index(30) # 접근만 하는 것이므로 가능
print(f'y = {y}') 
N = len(x) # 길이도 알 수 있다. 
print(f'N = {N}')