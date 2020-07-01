R = int(input("insert Raw : "))
C = int(input("insert Cal : "))

def spiral_array(R,C):

    array = [['X' for i in range(R) ] for j in range(C)]
    count = 0
    raw, col = 0, 0
    raw_dr, col_dr = 0, 1

    while(count < R*C):

        array[raw][col] = count

        raw += raw_dr
        col += col_dr

        if(raw in [-1,R] or col in [-1,C] or array[raw][col] != 'X'):

            raw -= raw_dr
            col -= col_dr
            raw_dr, col_dr = col_dr, -raw_dr

            raw += raw_dr
            col += col_dr

        count += 1

    for i in range(R):
        for j in range(C):
            print (array[i][j], end=" ")
        print ("\n")

spiral_array(R,C)