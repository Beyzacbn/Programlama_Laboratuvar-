#gönderilen parayı en az sayıda bozuk parayla geri verme

def para_üstü(n):
  para_100=0
  para_50=0
  para_20=0
  para_10=0
  para_5=0
  para_1=0
  sayi=0

  while(n>0) :
    if (n>100):
      n=n%100
      para_100=para_100+1
      print ("100 tl adedi : ", para_100)

      
    elif (n>50):
      n=n%50
      para_50=para_50+1
      print ("50 tl adedi : ", para_50)

    elif (n>20):
      sayi=int(n/20)
      n=n%20
      para_20=para_20+sayi
      print("20 tl adedi :",para_20)

    elif(n>10):
      temp=int(n/10)
      n=n%10
      para_10=para_10+1
      print ("10 tl adedi : ", para_10)
      
    elif (n>5):
      n=n%5
      para_5=para_5+1
      print ("5 tl adedi : " ,para_5)
      para_1=n
      print (" 1 tl adedi: " ,para_1)
    
    elif(n>1):
      n=int(n/1)
      para_1=para_1+n
      print(" 1 tl adedi: ", para_1)
      n=n-n
      

print(para_üstü(92))     


