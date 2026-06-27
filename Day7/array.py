import numpy as np
'''arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[1,2])
print(arr[:3,1:3])'''

'''arr = np.array([1,2,3,4,5])
print("Multiple by 2",arr*2)
print("Addition:",arr+5)
print("Subraction :",arr-4)
print("Division :",arr/4)
print("Floor Division :",arr//2)
print("Modulus:",arr%2)
print("Power:",arr**3)'''

'''arr = np.array([1,2,3,94,5])
print("Multiple by 2 :",np.multiply(2,arr))  
print("Addition by 5:",np.add(5,arr))
print("Subraction by 4 :",np.subtract(4,arr))
print("Division by 4:",np.divide(4,arr))
print("Floor Division by 2 :",np.floor_divide(2,arr))
print("Modulus by 2:",np.mod(2,arr))
print("Power by 3:",np.pow(3,arr))'''

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[6,7,8],[9,10,7]])
#marks.flags.writable = True;
marks = np.array([
    [95,100,35,52,75],
    [25,50,46,58,60]
])
marks[((marks > 50 ) & (marks <= 70))] = 4
print(marks)
    #print("Comparision :", marks[0:1,marks > 45])
    #print("Addition :",sum(arr1 ,arr2))
#print("Subraction :",(arr1,arr2))
'''print("Multiple :",arr1 @ arr2)
print(" Multiple:", np.matmul(arr2,arr1))
#print("Modulus :",np.mod(arr1,arr2))
print("mean:",np.mean(arr1))
print("median:",np.median(arr2))
print("variance :",np.var(arr1))
print("variance :",np.var(arr2))
print("min :",np.min(arr1))
print("max :",np.max(arr1))
print("standard :",np.std(arr1))
print("squrt :",np.sqrt(arr1))'''