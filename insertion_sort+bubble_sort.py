import random
def get_n_random_integer(n):
  #random.seed(100)
  numbers=[]
  for i in range(n):
    s=random.randint(-100,100)
    numbers.append(s)
  return numbers

def get_mean_for_n_integer(numbers):
  toplam=0
  kactane=0
  for sayi_in_numbers:
    toplam=toplam+sayi 
    kactane=kactane+1
  return toplam/kactane


def get_std_for_n_integer(numbers):
  toplam=0
  kactane=0
  ortalama=get_mean_for_n_integer(numbers)

  for sayi in numbers:
    toplam=toplam+(sayi-ortalama)**2
    kactane=kactane+1

  var_1=toplam/(kactane-1)
  std_1=var_1*0.5
  return std_1

def normalizasyon(numbers):
  new_numbers=[]
  ortalama=get_std_for_n_integer(numbers)
  standart_sapma=get_std_for_n_integer(numbers)

  for x in numbers:
    new_x=(x-ortalama)/standart_sapma
    new_numbers.append(new_x)
  return new_numbers

  sayilar=get_n_random_integer(5)
  ortalama=get_mean_for_n_integer(sayilar)
  standart_sapma=get_std_for_n_integer(sayilar)
  yeni_sayilar=normalizasyon(sayilar)
  print("sayilar: ",sayilar)
  print("ortalama: ",ortalama)
  print("standart_sapma: ",standart_sapma)
  print("yeni normalize edilmiş liste: ",yeni_sayilar)

def get_mean_one_std_neighbor_ratio(numbers):
    kacTane=0
    toplamKacSayi=0

    ortalama=get_std_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)

    low=ortalama-standart_sapma
    high=ortalama+standart_sapma

    for x in numbers:
      toplamKacSayi=toplamKacSayi+1
      if(x>low and x<high):
        kacTane=kacTane+1
    return kacTane/toplamKacSayi

    sayilar_1=get_n_random_integer(100)
    get_mean_one_std_neighbor_ratio(sayilar_1)

    print(yeni_sayilar)

    get_mean_for_n_integer(yeni_sayilar)
    get_std_for_n_integer(yeni_sayilar)

    sayilar_2=get_n_random_integer(5)
    print(sayilar_2)

def insertion(numbers):
  sayilar_2=numbers

  length_1=len(sayilar_2)
  print(sayilar_2)
  for i in range(1,length_1):
    for j in range(i,0,-1):
      if (sayilar_2[j]<sayilar_2[j-1]):
        #swap
        temp=sayilar_2[j-1]
        sayilar_2[j-1]=sayilar_2[j]
        sayilar_2[j]=temp
  print(sayilar_2)
  return sayilar_2

  print(sayilar_2)

  print([ i for i in range (10,-1,-1)]) #10-0

random.seed(100)
result_1=get_mean_of_swap_in_insertion(10,10)
random.seed(100)
result_2=get_mean_of_swap_in_bubble(10,10)
print("insertion: ", result_1)
print("bubble: ", result_2)

sayilar_1=get_n_random_integer(10)
sayilar_2=insertion(sayilar_1)
print("sıralanmış liste:",sayilar_2[0])
print("karşılaştırma sayısı: ",sayilar_2[1])
print("yer değiştirme sayısı: ",sayilar_2[2])

def get_mean_of_swap_in_insertion(numTrials,numInt):
  swap_sayilari=[]
  for i in range(numTrials):
    sayilar_1=get_n_random_integer(numInt)
    sayilar_2=insertion(sayilar_1)
    s_1=sayilar_2[2]
    swap_sayilari.append(s_1)
  #
  mean_1=get_mean_for_n_integer(swap_sayilari)
  std_1=get_std_for_n_integer(swap_sayilari)

  return numInt, int(mean_1),int(std_1)

def get_mean_of_swap_in_bubble(numTrials,numInt):
  swap_sayilari=[]
  
  for i in range(numTrials):
    sayilar_1=get_n_random_integer(numInt)
    s_1=bubbleSort(sayilar_1)
    swap_sayilari.append(s_1[1])
  #
  mean_1=get_mean_for_n_integer(swap_sayilari)
  std_1=get_std_for_n_integer(swap_sayilari)
  
  return numInt, int(mean_1),int(std_1)

def insertion(numbers):
  sayilar_2=numbers

  karsilastirma_sayisi=0
  yerdegistirme_sayisi=0
  length_1=len(sayilar_2)
  #print(sayilar2)
  for i in range(1,length_1):
    for j in range(i,0,-1):
      karsilastirma_sayisi+=1
      if(sayilar_2[j]<sayilar_2[j-1]):
        #swap
        yerdegistirme_sayisi+=1
        temp=sayilar_2[j-1]
        sayilar_2[j-1]=sayilar_2[j]
        sayilar_2[j]=temp

      else:
        break
  #print(sayilar_2)

  return sayilar_2,karsilastirma_sayisi,yerdegistirme_sayisi

def bubbleSort(arr):
  n=len(arr)
  karsilastirma_sayisi=0 #comparison
  yerdegistirme_sayisi=0  #swap
  #Traverse through all array elements
  for i in range(n):
    #Last i elements are already in place
    karsilastirma_sayisi+=1
    for j in range(0,n-i-1):
      #traverse the array from 0 to n-i-1
      #swap if the element found is greater
      #than the next element
      if arr[j]>arr[j+1]:
        yerdegistirme_sayisi+=1
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return karsilastirma_sayisi,yerdegistirme_sayisi

  sayilar_1=get_n_random_integer(10)
  print(sayilar_1)
  swap_sayisi=bubbleSort(sayilar_1)
  print(sayilar_1)
  print(swap_sayisi)

def get_mean_one_std_neighbor_ratio(numbers):
    kacTane=0
    toplamKacSayi=0

    ortalama=get_std_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)

    low=ortalama-standart_sapma
    high=ortalama+standart_sapma

    for x in numbers:
      toplamKacSayi=toplamKacSayi+1
      if(x>low and x<high):
        kacTane=kacTane+1
    return kacTane/toplamKacSayi

  sayilar=get_n_random_integer(5)
  ortalama=get_mean_for_n_integer(sayilar)
  standart_sapma=get_std_for_n_integer(sayilar)
  yeni_sayilar=normalizasyon(sayilar)
  print("sayilar: ", sayilar)
  print("ortalama: ",ortalama)
  print("standart_sapma :",standart_sapma)
  print("yeni_normalize_edilmiş_liste: ", yeni_sayilar)
  









