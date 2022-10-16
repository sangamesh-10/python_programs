string = input("Enter the string to check  : ")
# n = len(string)
# flag  = 0
# for i in range(n//2):
#     if string[i] != string[n-1-i]:
#         flag = 1
# if flag == 1:
#     print("not a palindrome")
# else:
#     print("Is palindrome")
rev = ""
for i in range(len(string)-1,-1,-1):
	rev += string[i]
print(rev)