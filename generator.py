import math
import os
import time
import numpy as np
import random

eliminate = 50


table = []
n = 3

temp = [1,2,3,4,5,6,7,8,9]
random.shuffle(temp)
table.append(temp)
for i in range(n**2-1):
    temp = []
    for j in range(n**2):
        temp.append(0)
    table.append(temp)


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
                    if table[i][j]==0:
                        print(" "+ "."+" | ", end="")
                    else:
                        print(" "+ str(table[i][j])+" | ", end="")
                else:
                    if table[i][j]==0:
                        print(" " + "." +" ", end="")
                    else:
                        print(" "+ str(table[i][j])+" ", end="")
            else:
                if table[i][j]==0:
                    print(" " + "." +" ", end="")
                else:
                    print(" "+ str(table[i][j])+" ", end="")

        if (i+1)%n==0 and i !=n**2-1:
            print(n**2*"---")


def check_valid_BOX(table, i , j):
    n = len(table)
    m = int(math.sqrt(n))
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
    n = len(table)
    if table[i][j] > n:
        return 0
    else:
        return check_valid_BOX(table, i,j)*check_valid_row(table, i,j)*check_valid_column(table, i,j)

def choose_position(table):
    n = len(table)
    for i in range(n):
        for j in range(n):
            if table[i][j]==0:

                return (i,j)


def backtracking_solver(table):
    n = len(table)
    Used_positions = []

    count_zeros = 0
    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                count_zeros += 1

    pos = 0
    while count_zeros != 0:
        if choose_position(table) == 1:
            return table
        else:

            i_cur, j_cur = choose_position(table)
            Used_positions.append([i_cur, j_cur])


            valid = 0
            k = 1
            while valid == 0:
                #print(Used_positions)
                #print(pos)
                #os.system('clear')
                #draw_board(int(math.sqrt(n)),table )
                table[i_cur][j_cur] = k

                valid = check_conditions_valid(table, i_cur, j_cur)
                k += 1
                if k > n and valid != 1:

                    table[i_cur][j_cur] = 0
                    count_zeros += 1

                    Used_positions.pop(-1)


                    i_cur, j_cur = Used_positions[-1][0],Used_positions[-1][1]
                    k = table[i_cur][ j_cur]


                    k += 1
                    table[i_cur][j_cur] = k
                    valid = check_conditions_valid(table,i_cur,j_cur)

            count_zeros -=1



backtracking_solver(table)

def remove(solved, eliminate):
    n = len(solved)
    used = []
    ind = 0
    while ind  < eliminate:

        i, j = random.randint(0,n-1), random.randint(0,n-1)
        if (i,j) not in used:
            #print((i,j))
            used.append((i,j))
            solved[i][j]= 0
            ind += 1
    return solved

#draw_board(3,table)
