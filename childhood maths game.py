#maths is fun
print("Hello\n \nwelcome to childhood maths game!!")
a=str(input(" \nThink a three digit number which have all different digits (tab yes for proceed): "))
if a=="yes" or a=="ok" or a=="sure":
 print(" \nNow,reverse the number and subtract it to the original number\n(the output should be modulus value) ")
 b=int(input(" \nTell me the last digit of final result: "))
 if b==9 :
  print("final is 99")
 elif b==8:
  print("final is 198")      
 elif b==7:      
    print("final is 297")
 elif b==6:
    print("final is 396")
 elif b==5:
    print("final is 495")
 elif b==4:
    print("final is 594")
 elif b==3:
    print("final is 693")
 elif b==2:
    print("final is 792")
 elif b==1:
    print("final is 891")
 elif b==0:
    print("final is 990")
 else:
   print("input shpuld be 1 digit/integer number from 0 to 9")


elif a=="no":
 print("ok sure")

else:
 print("give answer in (yes/no)")