""" 2.print from M to N number using for loop 
given two intergers numbers M and N write a program to print thr integers from M to N 
sample input
M=2
N=6 

output 
2
3
4
5
6 """
N=int(input("Enter the value N:"))
M=int(input("Enter the value M:"))
for i in range(N,M+1):
    print(i)