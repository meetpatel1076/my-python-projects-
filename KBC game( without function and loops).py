#KBC made from 'if-else'and 'list'
#it is made with basic understanding of python, will improve in future by loops and functions

print("_______Deviyon or Sajjano_______ \n \nWelcome to \"KBC\" , Kon Banega Crorepati\n ")

q= str(input("Before start enter your name: "))
w= int(input(" \nYour age(for eligibility): "))

lq=['1) After WW2 which country was suffered most','2) who invented computer','3) from the following IPL team which team win the least trophies','4) Most famous music instrument','5) Which of the following is not nation fastival','6) Which indian actor gives most flops in his caareer']
la=['a) Japan','a) Konrad Zuse','a) Royal Challengers Bangalore','a) Piano','a) Republic Day','a) Mithun Chakraborty']
lb=['b) The Soviet Union','b) Alan Turing','b) Kolkata Knight Riders','b) Guitar','b) Gandhi Jayanti','b) Akshay Kumar']
lc=['c) America','c) Charles Babbage','c) Mumbai Indians','c) Violin','c) Holi','c) Saharukh Khan']
ld=['d) Germany','d) John von Neumann','d) Panjab Super King','d) Sitar','d) Independence Day','d) Jackie Shroff']
  
if w>=13 and w<=45 :
    print(" \n",q,"you are elgible")
    r=str(input(" \nAre sure you want to proceed (yes/no): "))
    if r=="yes":
      q1 = input(f"{lq[0]}\n {la[0]}      {lb[0]}\n {lc[0]}    {ld[0]}\n Your answer: ")
      if q1=="b":
         print(" \nSahi Jwab",q,",amount winned:- $1000")
         p1=str(input("type yes to proceed: "))
         if p1=="yes":
              print(" ")
              q2 =input(f"{lq[1]}\n {la[1]}        {lb[1]}\n {lc[1]}    {ld[1]}\n   Your answer: ") 

              if q2=="c":
                 print(" \nSahi Jwab",q,",amount winned:- $2000")
                 p2=str(input("type yes to proceed: "))

                 if p2=="yes":
                    print(" ")
                    q3 =input(f"{lq[2]}\n {la[2]}     {lb[2]}\n {lc[2]}                  {ld[2]}\n   Your answer: ")
                
                    if q3=="d":
                       print(" \nSahi Jwab",q,",amount winned:- $4000")
                       p3=str(input("type yes to proceed: "))

                       if p3=="yes":
                          print(" ")
                          q4=input(f"{lq[3]}\n {la[3]}      {lb[3]}\n {lc[3]}     {ld[3]}\n   Your answer: ") 
                           
                          if q4=="a":
                             print(" \nSahi Jwab",q,",amount winned:- $8000")
                             p4=str(input("type yes to proceed: "))

                             if p4 =="yes":
                                print(" ")
                                q5=input(f"{lq[4]}\n {la[4]}     {lb[4]}\n {lc[4]}             {ld[4]}\n   Your answer: ")
                                
                                if q5=="c":
                                  print(" \nSahi Jwab",q,",amount winned:- $16000")
                                  p5=str(input("type yes to proceed: "))
                                   
                                  if p5=="yes":
                                     print(" ")
                                     q6=input(f"{lq[5]}\n {la[5]}     {lb[5]}\n {lc[5]}          {ld[5]}\n   Your answer: ")

                                     if q6=="a":
                                         print(" \n \nCONGRATULATIONS\nYOU WIN\n______7 cr..............__________")
                                     else:
                                        print(" \nyou winned:-$16000") 
                                else:
                                   print(" \nyou winned:-$8000")
                                   
                          else:
                             print(" \nyou winned:-$4000")


                    else:
                       print(" \nyou winned:-$2000")
              else:
                 print(" \nyou winned:-$1000")

      else:
         print(" \nBetter luck next time") 
    else:
       print(" \nThanks",q,"\nHave nice day")
      

     


else :
    print("you are not eligible")   