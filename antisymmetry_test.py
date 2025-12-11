from Matrix import Matrix

def anticheck(Matrix):
    anti = False
    row = len(Matrix.Neo)
    col = len(Matrix.Neo[0])
    for i in range(1,row):
        for j in range(1,col):
            if Matrix.get_val(i,j) == Matrix.get_val(j,i):
                anti = False
                break
            else:
                anti = True
    if anti:
        print("Your relation is antisymmetric!")
    else:
        print("Your relation is not antisymmetric!")    

def main():
    rows = int(input("Enter rows of Matrix: "))
    cols = int(input("Enter columns of Matrix: "))

    Reeves = Matrix(rows,cols)

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
    anticheck(Reeves)
main()