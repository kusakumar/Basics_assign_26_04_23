"""  9.rectangle -3 
write a program that reads tow numbers M and N and prints a rectangle m rows and N columns using number 

input:
2
3
output:
1 1 1 
2 2 2 """
M=int(input("Enter the value M:"))
N=int(input("Enter the value N:"))
for i in range(M,N+1):
    for j in range(1,N+1):
        print(i-1,end=' ')
    print()
