a = [38, 21, 53, 62, 19]
print(a[0])
# 38
print(a[2])
# 53
print(a[4])
# 19
del a[2]
print(a)
# [38, 21, 62, 19]
b = (38, 21, 53, 62, 19)
print(b[0])
# 38
r = range(0, 10, 2)
print(r[2])
# 4
hello = 'Hello, world!'
print(hello[7])
# w
print(hello[-4])
# r
a = [38, 21, 53, 62, 19]
print(a)
# [38, 21, 53, 62, 19]
print(a.__getitem__(1))
# 21
print(a[-1])
# 19
print(a[-5])
# 38
print(a[4]) # 마지막 문자 출력
# 19
print(a[len(a) - 1]) # 마지막 요소(인덱스 4) 출력
# 19
b = (38, 21, 53, 62, 19)
print(b[-1])
# 19
r = range(0, 10, 2)
print(r[-3])
# 6
