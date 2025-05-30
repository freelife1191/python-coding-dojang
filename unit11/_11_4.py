# List slicing examples
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:4]) # 인덱스 0부터 3까지 잘라서 새 리스트를 만듦
# [0, 10, 20, 30]
print(a[0:10]) # 인덱스 0부터 9까지 잘라서 새 리스트를 만듦
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[1:1]) # 인덱스 1부터 0까지 잘라서 새 리스트를 만듦
# []
print(a[1:2]) # 인덱스 1부터 1까지 잘라서 새 리스트를 만듦
# [10]
print(a[4:7]) # 인덱스 4부터 6까지 잘라서 새 리스트를 만듦
# [40, 50, 60]
print(a[4:-1]) # 인덱스 4부터 -2까지 요소 5개를 가져옴
# [40, 50, 60, 70, 80]
print(a[2:8:3]) # 인덱스 2부터 3씩 증가시키면서 인덱스 7까지 가져옴
# [20, 50]
print(a[2:9:3]) # 인덱스 2부터 3씩 증가시키면서 인덱스 8까지 가져옴
# [20, 50, 80]
print(a[:7]) # 리스트 처음부터 인덱스 6까지 가져옴
# [0, 10, 20, 30, 40, 50, 60]
print(a[7:]) # 인덱스 7부터 마지막 요소까지 가져옴
# [70, 80, 90]
print(a[:]) # 리스트 전체를 가져옴
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[:7:2]) # 리스트의 처음부터 인덱스를 2씩 증가시키면서 인덱스 6까지 가져옴
# [0, 20, 40, 60]
print(a[7::2]) # 인덱스 7부터 2씩 증가시키면서 리스트의 마지막 요소까지 가져옴
# [70, 90]
print(a[::2]) # 리스트 전체에서 인덱스 0부터 2씩 증가시키면서 요소를 가져옴
# [0, 20, 40, 60, 80]
print(a[::]) # 리스트 전체를 가져옴
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[5:1:-1])
# [50, 40, 30, 20]
print(a[::-1])
# [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
print(a[0:len(a)]) # 시작 인덱스에 0, 끝 인덱스에 len(a) 지정하여 리스트 전체를 가져옴
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[:len(a)]) # 시작 인덱스 생략, 끝 인덱스에 len(a) 지정하여 리스트 전체를 가져옴
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Tuple slicing examples
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
print(b[4:7]) # 인덱스 4부터 6까지 요소 3개를 가져옴
# (40, 50, 60)
print(b[4:]) # 인덱스 4부터 마지막 요소까지 가져옴
# (40, 50, 60, 70, 80, 90)
print(b[:7:2]) # 튜플의 처음부터 인덱스를 2씩 증가시키면서 인덱스 6까지 가져옴
# (0, 20, 40, 60)

r = range(10)
print(r)
# range(0, 10)
print(r[4:7]) # 인덱스 4부터 6까지 숫자 3개를 생성하는 range 객체를 만듦
# range(4, 7)
print(r[4:]) # 인덱스 4부터 9까지 숫자 6개를 생성하는 range 객체를 만듦
# range(4, 10)
print(r[:7:2]) # 인덱스 0부터 2씩 증가시키면서 인덱스 6까지 숫자 4개를 생성하는 range 객체를 만듦
# range(0, 7, 2)
print(list(r[:7:2]))
# [0, 2, 4, 6]

hello = 'Hello, world!'
print(hello[2:9]) # 인덱스 2부터 인덱스 8까지 잘라서 문자열을 만듦
# 'llo, wo'
print(hello[2:]) # 인덱스 2부터 마지막 요소까지 잘라서 문자열을 만듦
# 'llo, world!'
print(hello[:9:2]) # 문자열의 처음부터 인덱스를 2씩 증가시키면서 인덱스 8까지 잘라서 문자열을 만듦
# 'Hlo o'
print(range(10)[slice(4, 7, 2)])
# range(4, 7, 2)
print(range(10).__getitem__(slice(4, 7, 2)))
# range(4, 7, 2)

s = slice(4, 7) # 인덱스 4부터 6까지 자르는 slice 객체 생성
print(a[s])
# [40, 50, 60]
r = range(10)
print(r[s])
# range(4, 7)
hello = 'Hello, world!'
print(hello[s])
# 'o, '
a[2:5] = ['a', 'b', 'c'] # 인덱스 2부터 4까지 값 할당
print(a)
# [0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a']    # 인덱스 2부터 4까지에 값 1개를 할당하여 요소의 개수가 줄어듦
print(a)
# [0, 10, 'a', 50, 60, 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e'] # 인덱스 2부터 4까지 값 5개를 할당하여 요소의 개수가 늘어남
print(a)
# [0, 10, 'a', 'b', 'c', 'd', 'e', 50, 60, 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b', 'c'] # 인덱스 2부터 2씩 증가시키면서 인덱스 7까지 값 할당
print(a)
# [0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:5]    # 인덱스 2부터 4까지 요소를 삭제
print(a)
# [0, 10, 50, 60, 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:8:2]    # 인덱스 2부터 2씩 증가시키면서 인덱스 6까지 삭제
print(a)
# [0, 10, 30, 50, 70, 80, 90]