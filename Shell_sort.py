def shellSort(arr):
  n=len(arr)
  gap=n//2
  karsilastirmasayisi=0
  yerdegistirmesayisi=0
  while(gap > 0):
    for i in range (gap,n):
      karsilastirmasayisi+=1
      temp=arr[i]
      j=i
      while (j>= gap and arr[j-gap]>temp) :
        karsilastirmasayisi+=1
        arr[j]=arr[j-gap]
        j-=gap
        yerdegistirmesayisi+=1
      arr[j]=temp
    gap //=2
  return karsilastirmasayisi, yerdegistirmesayisi

  arr=[12,34,54,2,3,1]
  mx=shellSort(arr)
  print(mx,arr)
