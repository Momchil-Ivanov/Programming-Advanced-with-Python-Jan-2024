rows, cols = [int(el) for el in input().split(',')]

matrix = []
m_row = 0
m_col = 0

cheese = 0

for row in range(rows):
    matrix.append([str(el) for el in input()])
    if 'M' in matrix[row]:
        m_row = row
        m_col = matrix[row].index('M')
    if 'C' in matrix[row]:
        cheese += matrix[row].count('C')


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'danger':
        print('Mouse will come back later!')
        break
    matrix[m_row][m_col] = '*'
    m_row += directions[command][0]
    m_col += directions[command][1]
    if (not 0 <= m_row < rows) or (not 0 <= m_col < cols):
        m_row -= directions[command][0]
        m_col -= directions[command][1]
        matrix[m_row][m_col] = 'M'
        print(f'No more cheese for tonight!')
        break

    if matrix[m_row][m_col] == 'C':
        cheese -= 1
        matrix[m_row][m_col] = '*'
        if cheese == 0:
            matrix[m_row][m_col] = 'M'
            print(f'Happy mouse! All the cheese is eaten, good night!')
            break
    elif matrix[m_row][m_col] == '@':
        m_row -= directions[command][0]
        m_col -= directions[command][1]
        matrix[m_row][m_col] = 'M'
    elif matrix[m_row][m_col] == "*":
        matrix[m_row][m_col] = 'M'
    elif matrix[m_row][m_col] == 'T':
        matrix[m_row][m_col] = 'M'
        print(f'Mouse is trapped!')
        break

for row in matrix:
    print(''.join([str(el) for el in row]))
