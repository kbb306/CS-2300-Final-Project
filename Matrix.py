
class Matrix():
    def __init__(self, row, col):
        row = abs(int(row))
        col = abs(int(col))
        self.Neo = []
        for i in range(row):
            listinator = [0 for j in range(col)]
            #print(listinator)
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
        elif len(Smith) < len(self.Neo[row - 1]):
            while len(Smith) < len(self.Neo[row - 1]):
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
        if len(Morpheus) > len(self.Neo[col - 1]):
            raise ValueError("Input has too many elements")
        while len(Morpheus) < len(self.Neo[col - 1]):
            Morpheus.append(0)
        for each in self.Neo:
            each[col-1] = Morpheus[self.Neo.index(each)]

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
        Trinity = abs(int(Trinity))
        if not isinstance(Trinity,int):
            raise ValueError(f"{Trinity} is not an integer")
        if (row > len(self.Neo) or col > len(self.Neo)):
            raise ValueError(f"Index {row},{col} out of range.")
        else:
            self.Neo[row -1][col - 1] = Trinity

    def print_matrix(self):
        for each in self.Neo:
            print(each)


    
        
        