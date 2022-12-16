
#Piotr Warzachowski

def is_complete(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return False
    return True

def find_first_free_cell(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return i, j


def is_valid(board, n):
    numbers = []
    magic_constant = int((n * (n*n + 1))/2)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                if board[i][j] in numbers:
                    return False
                else:
                    numbers.append(board[i][j])
              
    columns = [list(arr) for arr in zip(*board)]
    diagonal = [board[i][i] for i in range(len(board))]
    anti_diagonal = [board[i][len(board)-i-1] for i in range(len(board))]

    for i in range(n):
        if 0 not in board[i]:
            if sum(board[i])!=magic_constant:
                return False
    
    for i in range(n):
        if 0 not in columns[i]:
            if sum(columns[i]) !=magic_constant:
                return False
    
    if 0 not in diagonal:
        if sum(diagonal) != magic_constant:
            return False

    if 0 not in anti_diagonal:
        if sum(anti_diagonal) != magic_constant:

            return False
    
    
    
    return True
def back_track(matrix, n):

    if is_complete(matrix, n): return matrix

    i, j = find_first_free_cell(matrix, n)
    for num in range(1,n*n + 1):
        matrix[i][j] = num
        if is_valid(matrix,n):
            result = back_track(matrix, n)
            if is_complete(result, n):
                return result

        matrix[i][j] = 0
        
    return matrix


n = 3
matrix = [ [0 for i in range(n)] for j in range(n) ]
print(back_track(matrix, n))
