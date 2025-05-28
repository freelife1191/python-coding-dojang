start, stop = map(int, input().split())
list = [ 2 ** i for i in range(start, stop + 1)]
# list.pop(-2)
# list.pop(1)
del list[-2]
del list[1]
print(list)