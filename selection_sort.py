#Selection sort kodu

def my_selection_sort(array):
  for i in range(len(array)-1,0,-1):
    positionOfMax=0
    for location in range(1,i+1):
      #print("j: ",location, "i: ",end=" ")
      if(array[location]>array[positionOfMax]):
        positionOfMax=
    temp=array[location]
    array[location]=array[positionOfMax]
    array[positionOfMax]= temp
    
   return array	


#İkili arama kodu

def binary_search(array,search):
  first=0
  last=len(array)-1 #indis dışına çıkmamak için
  found=False
  step=0  
  while(first<=last and not found):
    
    mid=(first+last)//2
    print("first-last : ",first,last)
    step+=1  #kaçıncı adımda buldu
    if(array[mid]==search):
      found=True
    else:
      if(array[mid]>search):
        last=mid-1
      else:
        first=mid+1
  
  return found,mid,step


array=[21,16,13,44,25,28,7,19,14]
print(selection_sort(array))
print(binary_search(array,28))
