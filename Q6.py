""" 6.Right angles triangle using for loop 
write a program that reads a number N and prints a right angled triangle of N rows using stars 
input
4 

output 
*
* *
* * *
* * * """
M=int(input("Enter the value M:"))
for i in range(1,M+1):
    for j in range(1,i+1):
        print(" *",end='')
    print()
print("\r")
#Method2
for j in range(1, M+1):
    print("* " * j)