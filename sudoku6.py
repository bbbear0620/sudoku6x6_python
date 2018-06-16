#import numpy as np
sudoku = [[3,0,0,0,4,0],
          [0,0,4,0,0,0],
          [0,0,6,0,0,2],
          [0,5,0,0,1,0],
          [0,0,0,0,0,0],
          [0,6,0,0,0,1]]


def not_exist_row(row,col,num):#数字num在行中不存在
    if num in sudoku[row]:
        return False
    else:
        return True

def not_exist_col(row,col,num):#数字num在列中不存在
    temp = []
    for i in range(6):
        if sudoku[i][col] != 0:
            temp.append(sudoku[i][col])
    if num in temp:
        return False
    else:
        return True

def not_exist_area(row,col,num):#数字num在宫中不存在
    row_area = ((int)(row/2))*2
    col_area = ((int)(col/3))*3
    for temp_row in range(row_area,row_area+2):
        for temp_col in range(col_area,col_area+3):
            if num == sudoku[temp_row][temp_col]:
                return False
    return True

'''def not_exist_diagonal(row,col,num):#当前位置是否不处于对角线上，若处于对角线上数字num是否不存在在对角线中
    if row+col!=5 and row!=col:
        return True
    if row+col == 5:
        for i in range(6):
            if num == sudoku[i][5-i]:
                return False
    if row == col:
        for j in range(6):
            if num == sudoku[j][j]:
                return False
    return True'''

def next_bank(row,col):
    for t in range(col+1,6):
        if sudoku[row][t] == 0:
            return row,t
    for next_row in range(row+1,6):
        for next_col in range(6):
            if sudoku[next_row][next_col] == 0:
                return next_row,next_col
    return -1,-1

def big_loop(row,col):
    if sudoku[row][col] == 0:
        for num in range(1,7):
            if not_exist_col(row,col,num) and not_exist_row(row,col,num) and not_exist_area(row,col,num):#and not_exist_diagonal(row,col,num):
                sudoku[row][col] = num
                #print(sudoku)
                next_row,next_col = next_bank(row,col)
                if next_row == -1:
                    return True
                else:
                    error_show = False
                    error_show = big_loop(next_row,next_col)
                    if not error_show :
                        sudoku[row][col] = 0
                    else:
                        return True
def begins():
    print('create your sudoku:')
    for i in range(6):
        x = input()
        xlist = x.split(' ')
        xlist = [(int)(xlist[k]) for k in range(6)]
        sudoku[i] = xlist
    if sudoku[0][0] == 0:
        big_loop(0,0)
    else:
        frow,fcol = next_bank(0,0)
        big_loop(frow,fcol)
    for x in range(6):
        print(sudoku[x])
begins()
