from OopsDemo import Calculator


class ChildImp(Calculator):
    num2 = 200

    # If this is not declared summation method won't execute due to run time variables used in class
    def __init__(self):
        Calculator.__init__(self,2,4)

    #child class inheriting the parent Methods/Variables
    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildImp()
print(obj.getCompleteData())