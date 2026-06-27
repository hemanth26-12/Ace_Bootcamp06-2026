class Student:
    fee_hike = 1.02
    def __init__(self,name,roll_no,branch,fee,yjo):
        self.id = name
        self.roll_no = roll_no
        self.branch = branch
        print("name :",self.id)
        print("roll_Number :",self.roll_no)
        print("Branch :",self.branch)
        print("-"*30)
    @classmethod
    def hike(cls):
        return "Iam a class method..."
    
    @staticmethod
    def result(fname,lname):
        return {fname} + {lname}
    
        '''match yjo:
            case 2022:
                if(cur__y - y):
                    pass'''

    def name(self):

        print(self.name) 
    
   # def __repr__(self):
       # return f'{self.id},{self.roll_no},{self.branch}'
    #def __str__(self):
        #return f'{self.id},{self.roll_no},{self.branch}'
   

        
s2=Student.hike()

s2 = Student.result("hemanth","01")
print(s2)
s1 = Student("Hemanth","24Ag1a6624","CSM",10000,2024)
print(s1.name())
print(s1)
print("-"*30)
'''s2 = Student("Hemanth","24Ag1a6624","CSM")
print(s2)
print("-"*30)
print(id(s1))
print(id(s2))'''

'''str1 = "Hello"
print(id(str1))
print(str)
print(int.__add__(1,2))
print("1" + "2")
print(str.__add__("1","2"))'''



