class Demo:

    def __init__(self,name,rno,branch):
        self.name = name
        self.rno = rno
        self.branch= branch
    @property
    def from_branch(self):
        return self.branch,self.name,self.rno
    @from_branch.setter
    def from_branch(self,branch):
        self.branch = branch
    @from_branch.deleter
    def from_branch(self):
        self.branch = None

c1 = Demo("Hemanth","24Ag1a6624","CSM")
print(c1.branch)
c1.from_branch = "CSD"
print(c1.branch)

del c1.from_branch
print(c1.branch)


 