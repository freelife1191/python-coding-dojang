col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            continue
        else:
            matrix[i][j] = 0 # 0을 넣은 뒤에는 요소 주변 8개를 탐색하면서 *이면 요소를 1개씩 증가
            # range에서 생성한 숫자의 마지막 값은 끝나는 값보다 1 작은데
            # 탐색을 위해서 한 칸 아래까지 더 반복해야 하므로 i + 1이 아닌 i + 2가 되어야 함
            for y in range(i - 1, i + 2): # 한 칸 위부터 한 칸 아래까지 반복
                for x in range(j - 1, j + 2): # 한 칸 앞(왼쪽)부터 한 칸 뒤(오른쪽)까지 반복
                    if y < 0 or x < 0 or y >= row or x >= col: # 리스트의 범위를 벗어나면 건너뛰기
                        continue
                    elif matrix[y][x] == '*':
                        matrix[i][j] += 1

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()

# for i in matrix:
#     for j in i:
#         print(j, end='')
#     print()