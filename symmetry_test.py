from Matrix import Matrix
from antisymmetry_test import anticheck
rows = int(input("Enter rows of matrix: "))
cols = int(input("Enter columns of matrix: "))
Sym = True
Reeves = Matrix(rows,cols)
Seveer = Matrix(cols,rows)

for i in range(rows):
    inrow = []
    for j in range(cols):
        val = input(f"Enter next value in row {i+1}: ")
        if int(val) > 0:
            val = 1
        else:
            val = 0
        inrow.append(int(val))
    Reeves.set_row((i+1),inrow)
    try:
        Seveer.set_col((i+1),inrow)
    except ValueError:
        Sym = False
        break
if Reeves.Neo == Seveer.Neo:
    Sym = True
else:
    Sym = False
if Sym:
    print("Your relation is symmetrical!")
else:
    print("Your relation is not symmetrical!")
anticheck(Reeves)