import Matrix

row = input("Enter rows of Matrix")
col = input("Enter columns of Matrix")

Watchowski = Matrix(row,col)

for each in Watchowski.Neo:
    inrow = input(f"Enter row {Watchowski.Neo.index(each) + 1} of matrix")
    Watchowski.set_row(inrow)

check = []
