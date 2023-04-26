""" 5.given two integers M and N write a program to print a solid rectangle pattern of rows and N column using the asterisk character(*)

Input:
2
3

output
* * *
* * * """

N=int(input("Enter the value N:"))
M=int(input("Enter the value M:"))
for i in range(1,N+1):
 print("* "*M)