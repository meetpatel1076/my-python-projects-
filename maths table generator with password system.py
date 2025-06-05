while True :
   num = int(input("enter the password to acces the table generator:\n \n"))
   
   if num == 1001:
      print(" \nyou enter right password")
      break
   else:
      print(" \n \nyou enter wrong password, try again\n ")
      continue

print(" \n ")

i = int(input("____________Welcome___________ \n \nWhich table you want to print: "))
y= int(input("from: "))
z= int(input("till: "))
for j in range(y,z+1):
   print(i,"X",j,"=",i*j)

#part 2 for table with while function


# k = int(input("enter which table you want to print: "))
# i= int(input("from: "))
# f = int(input("till:"))
# while i <= f:
#   print(k,"X",i,"=",k*i)
#   i = i+1
#   if i == 11:
#      break
  
# print("general table end here (experimental)")


