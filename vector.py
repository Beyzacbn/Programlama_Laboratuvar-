#skaler çarpım
def my_Vector_Scalar_Product(alpha,v):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=alpha*v[i]
  return my_result

#vektörel çarpım
def my_Vectors_Inner_Product(v,w):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]*w[i]

  t=0
  for i in range (size)
    t=t+my_result[i]
  return t 

#çıkarma
def my_Vector_Substraction(v,w):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]-w[i]
  return my_result

#vektörel toplam
def my_Vector_Addition(v,w):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]+w[i]
  return my_result


  a=[1,2,3,2,4,6]
  b=[11,22,33,22,44,66]
  alpha=5
  beta=10
  print(my_Vector_Addition(a,b))
  print(my_Vector_Substraction(a,b))
  print(my_Vektor_Scalar_Product(alpha,a))
  print(Vector_Scalar_Product(beta,b))
  
  
