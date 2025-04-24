a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(len(a))
# 10
b = (38, 76, 43, 62, 19)
print(len(b))
# 5
print(len(range(0, 10, 2)))
# 5
hello = 'Hello, world!'
print(len(hello))
# 13
hello = '안녕하세요'
print(len(hello))
# 5
hello = '안녕하세요'
print(len(hello.encode('utf-8')))
# UTF-8에서 한글 글자 하나는 3바이트
# 15