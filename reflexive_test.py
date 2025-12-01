from Matrix import Matrix

row = int(input("Enter rows of Matrix: "))
col = int(input("Enter columns of Matrix: "))

Watchowski = Matrix(row,col)

for i in range(row):
    inrow = []
    for j in range(col):
        inrow.append(int(input("Enter next value: ")))
    Watchowski.set_row(row,inrow)

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