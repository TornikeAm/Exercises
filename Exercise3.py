import numpy as np

def bomberman(n,grid,row,column):
    ### at first second bomberman does nothing and we return initialized grid
    if n == 1 :
        return grid
    # on even seconds all the points will be filled with bombs
    if n %2 ==0: return [ 'O'*column for i in range(row)]

    ## since we know that at even seconds grid is filled wth bombs
    ### we need to remove that seconds and work with alternative cases
    n//=2
    for i in range((n+1) %2 +1):
        newgrid = [['O']*column for i in range(row)]
        #detonationt
        def detonate(x,y):
            # if its not out of bounds then detonete
            if 0 <=x<row and 0 <=y<column:
                newgrid[x][y] = '.'

        adjacent_x = [0,0,0,1,-1]
        adjacent_y= [0,-1,1,0,0]

        for x in range(row):
            for y in range(column):
                #check if the bobm is current cell
                if grid[x][y] == 'O':
                    for i,j in zip(adjacent_x,adjacent_y):
                        # it will change current cell to empty
                        detonate(x+i,y+j)

        grid = newgrid

    return [''.join(x) for x in grid]


grid = np.array([['.','.','.','O','.'],
        ['.','O','.','.','.'],
        ['.','.','.','0','.'],
        ['.','.','.','.','.'],
        ['.','O','.','.','.'],
        ['.','.','.','.','.']])

n = 3
print(bomberman(n,grid,grid.shape[0],grid.shape[1]))