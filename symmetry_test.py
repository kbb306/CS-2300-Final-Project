from Matrix import Matrix
rows = int(input("Enter rows of matrix: "))
cols = int(input("Enter columns of matrix: "))

Reeves = Matrix(rows,cols)
Seveer = Matrix(cols,rows)

for i in range(rows):
    inrow = []
    for j in range(cols):
        inrow.append(int(input(f"Enter next value in row {i+1}: ")))
    Reeves.set_row((i+1),inrow)
    try:
        Seveer.set_col(i+1,inrow)
    except ValueError:
        print("Your matrix is not symmetrical")
        break
if Reeves.Neo == Seveer.Neo:
    print("Your matrix is symmetrical!")
else:
    print("Your matrix is not symmetrical!")