""" 3.sum of Numbers from M to N using for loop 
given two integers M and N write a program to print thr sum of the numbers from M to N

sample input 
2
6

output 
20 """
M=int(input("Enter the value M:"))
N=int(input("Enter the value N:"))
Tsum=0
for i in range(M,N+1):
    Tsum+=i
print(Tsum)

#Method2

#m = int(input("Enter a number: "))
#n = int(input("Enter a second number: "))
print(sum(range(M, N+1)))