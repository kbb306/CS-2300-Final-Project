import Matrix

row = input("Enter rows of Matrix")
col = input("Enter columns of Matrix")

Watchowski = Matrix(row,col)

for each in Watchowski.Neo:
    inrow = input(f"Enter row {Watchowski.Neo.index(each) + 1} of matrix")
    Watchowski.set_row(inrow)

check = []

Reflexive = True
for each in Watchowski.Neo:
    get = Watchowski.get_val(Watchowski.Neo.index(each),Watchowski.Neo.index(each))
    if get < 1:
        Reflexive = False
        break
if Reflexive:
    print("Your matrix is reflexive.")
else:
    print("Your matrix is not reflexive.")