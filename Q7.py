""" 7.Right angled triangle  
write a program that reads a number N and prints a right angled triangle of N rows using stars (*) and pluses(+) 
input 
4 

output 
* 
* * 
* * * 
+ + + + """
M=int(input("Enter the value M:"))
for i in range(1,M):
    for j in range(1,i+1):
        print(" *",end='')
    print()
print("+ "*M)

#Method2
print("\r")
for j in range(1, M):
    print("* " * j)
print("+ "*M)