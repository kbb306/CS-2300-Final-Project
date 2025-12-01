
class Matrix():
    def __init__(self, row, col):
        row = abs(int(row))
        col = abs(int(col))
        self.Neo = []
        for i in range(row - 1):
            listinator = [j for j in range(col - 1)]
            self.Neo.append(listinator)

    def get_row(self,row):
        row = abs(int(row))
        return self.Neo[row - 1]
    def set_row(self,row,Smith):
        row = abs(int(row))
        if not all(isinstance(item, int) for item in Smith):
            raise ValueError("Input has non-integers")
        if len(Smith) == len(self.Neo[row - 1]):
            self.Neo[row - 1] = Smith
        elif len(Smith) < len(self.Neo[row]):
            while len(Smith) < len(self.Neo[row]):
                Smith.append(0)
            self.Neo[row - 1] = Smith
        else:
            raise ValueError("Input has too many elements")
        
    def get_col(self,col):
        col = abs(int(col))
        Morpheus = []
        for each in self.Neo:
            Morpheus.append(each[col-1])
        return Morpheus
    def set_col(self,col,Morpheus):
        col = abs(int(col))
        if not all(isinstance(item, int) for item in Morpheus):
            raise ValueError("Input has non-integers")
        if len(Morpheus) > self.Neo[0]:
            raise ValueError("Input has too many elements")
        while len(Morpheus) < len(self.Neo[0]):
            Morpheus.append(0)
        for each in self.Neo:
            each[col] = Morpheus[self.Neo.index(each)]

    def get_val(self,row,col):
        row = abs(int(row))
        col = abs(int(col))
        if (row > len(self.Neo) or col > len(self.Neo)):
            raise ValueError(f"Index {row},{col} out of range.")
        else:
            return self.Neo[row -1][col -1]
    def set_val(self,row,col,Trinity):
        row = abs(int(row))
        col = abs(int(col))
        if not isinstance(Trinity,int):
            raise ValueError(f"{Trinity} is not an integer")
        if (row > len(self.Neo) or col > len(self.Neo)):
            raise ValueError(f"Index {row},{col} out of range.")
        else:
            self.Neo[row -1][col - 1] = Trinity

    def print_matrix(self):
        for each in self.Neo:
            print(each,"\n")


    
        
        