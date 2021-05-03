import math

table = [[ 0, 0, 4,   0, 0, 0,   0, 6, 7 ],
         [ 3, 0, 0,   4, 7, 0,   0, 0, 5 ],
         [ 1, 5, 0,   8, 2, 0,   0, 0, 3 ],

         [ 0, 0, 6,   0, 0, 0,   0, 3, 1 ],
         [ 8, 0, 2,   1, 0, 5,   6, 0, 4 ],
         [ 4, 1, 0,   0, 0, 0,   9, 0, 0 ],

         [ 7, 0, 0,   0, 8, 0,   0, 4, 6 ],
         [ 6, 0, 0,   0, 1, 2,   0, 0, 0 ],
         [ 9, 3, 0,   0, 0, 0,   7, 1, 0 ] ]


def draw_board(n, table):
    """
    n -> size of the board
    """
    print()
    print("###################")
    print("Solving this table:")
    print("###################")
    print()
    for i in range((n)**2):
        for j in range(n**2):
            if j != n**2-1:
                if (j+1)%n==0:
                    print(" "+ str(table[i][j])+" | ", end="")
                else:
                    print(" " +str(table[i][j]) +" ", end="")
            else:
                print(" " +str(table[i][j]) +" ")
        if (i+1)%n==0 and i !=n**2-1:
            print(n**2*"---")


def check_valid_BOX(table, i , j):
    n = len(table)
    m = math.sqrt(n)
    Try = []
    Big_x, Big_y = i//m, j//m
    for x in range(m*Big_x, m*(Big_x + 1)):
        for y in range(m*Big_y, m*(Big_y+1)):
            if table[x][y] in Try and table[x][y] !=0:
                return 0
            elif table[x][y] not in Try and table[x][y] !=0:
                Try.append(table[x][y])

    return 1

def check_valid_row(table, i, j):
    n = len(table)
    m = int(math.sqrt(n))
    Try = []
    for x in range(n):
        if table[i][x] in Try and table[i][x] !=0:
            return 0
        elif table[i][x] not in Try and table[i][x] !=0:
            Try.append(table[i][x])

    return 1

def check_valid_column(table, i, j):
    n = len(table)
    m = math.sqrt(n)
    Try = []
    for x in range(n):
        if table[x][j] in Try and table[x][j] !=0:
            return 0
        elif table[x][j] not in Try and table[x][j] !=0:
            Try.append(table[x][j])

    return 1

def check_conditions_valid(table, i,j):
    return check_valid_BOX(table, i,j)*check_valid_row(table, i,j)*check_valid_column(table, i,j)


check_conditions_valid(table, 0 ,0 )
