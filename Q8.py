"""   8.two right angled triangles  
write a program that reads a number N and print two right angled triangles of N rows using numbers strating from 1 

input 
4 

sample 
1
22
333
4444
1
22
333
4444   """
M=int(input("Enter the value M:"))
for i in range(1,M+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
for k in range(1,M+1):
    for n in range(1,k+1):
        print(k,end='')
    print()