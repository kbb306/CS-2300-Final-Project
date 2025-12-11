from Matrix import Matrix

row = int(input("Enter rows of Matrix: "))
col = int(input("Enter columns of Matrix: "))

Watchowski = Matrix(row,col)

for i in range(row):
    inrow = []
    for j in range(col):
        inrow.append(int(input(f"Enter next value in row {i+1}: ")))
    Watchowski.set_row((i+1),inrow)

print("Your matrix is: ")
Watchowski.print_matrix()

Reflexive = True
for each in Watchowski.Neo:
    print(f"Getting value at {Watchowski.Neo.index(each) + 1},{Watchowski.Neo.index(each)+ 1}")
    get = Watchowski.get_val((Watchowski.Neo.index(each) + 1),(Watchowski.Neo.index(each)+ 1))
    if get < 1:
        Reflexive = False
        break
if Reflexive:
    print("Your relation is reflexive.")
else:
    print("Your relation is not reflexive.")