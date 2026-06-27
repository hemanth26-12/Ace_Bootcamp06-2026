class Demo:
    def __init__(self,name,rno,branch):
        self.name = name
        self.rno = rno
        self.branch= branch

    def get_branch(self):
        return self.branch,self.name,self.rno
    def set_branch(self,branch):
        self.sbranch = branch

    def del_branch(self):
        self.branch = None

c1 = Demo("Hemanth","24Ag1a6624","CSM")
c1.set_branch("CSD")

print(c1.get_branch())
c1.del_branch()
print(c1.get_branch())

