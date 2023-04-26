""" solid right angled Triangle

given an interger number N as input write a program to print the right-angled triangle pattern of n lines using asterisk(*) character.

input: 4
output:
*
* *
* * *
* * * *  """

M=int(input("Enter the value M:"))
for i in range(M+1):
    print("* "*i)

print("\r")
#reverse pattern
for i in range(M+1):
    print("* "*(M-i))