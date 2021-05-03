import generator as gen
import solver as sol
import random
import time
import sys
n = sys.argv[1]
n = int(n)



table = []
eliminate = 50
print(eliminate)
temp = [i+1 for i in range(n**2)]

random.shuffle(temp)
table.append(temp)
for i in range(n**2-1):
    temp = []
    for j in range(n**2):
        temp.append(0)
    table.append(temp)


table = sol.backtracking_solver(table)
sol.draw_board(n,table)
table_to_solve = gen.remove(table, eliminate)

sol.draw_board(n, table_to_solve)
time.sleep(2)


solved_table = sol.backtracking_solver(table_to_solve)
sol.draw_board(n, solved_table)
