num = int(input("enter the number of rows:"))

for i in range(0, num):   
        for j in range(0, i + 1):              
            print("*", end=" ")
        print() 

for i in range(0, num):   
        for j in range(0, i + 1):              
            print(j, end=" ")
        print()  
 
for i in range(1, num+1):
      for j in range(1, i + 1):  
         print(j, end=" ")
      print()      
