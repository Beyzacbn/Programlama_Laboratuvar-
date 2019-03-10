#kendisine gönderilen listenin frekans tablosunu geri döndüren fonksiyon

my_list=[2,3,5,8,6,4,3,6,2,3,5,6]
#liste
a=[6,3] 
#tupple veri değiştirilmez
#son halini biliyorsan kullanmak mantıklı 
b=(6,3) 
#sözlük
c={6:3} 


#sözlük 
my_list=[2,3,5,8,6,4,3,6,2,3,5,6]
def my_freq(list):
  freq_dict={}
  for i in list:
    if(i in freq_dict):
      freq_dict[i]=freq_dict[i]+1
    else:
      freq_dict[i]=1
  return freq_dict

print(my_freq(my_list))  



#liste 
def freq_list(list):
  result=[]
  for i in range(len(list)):
    a=False
    for j in range(len(result)):
      if(result[j][0]==list[i]):
        result[j][1]+=1
        a=True
    if(a==False):
      result.append([list[i],1])
  return result

print(freq_list(my_list))  
