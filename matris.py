#matrislerde toplama işlemi
def my_matrix_addition(m_1,m_2):
  result=[]
  for row in range (len(m_1)):
    result.append([])
    for column in range (len(m_1[0])):
      #print(m_1[row][column],end=" ")
      result[row].append(m_1[row][column]+m_2[row][column])
    #print()
  return result
matrix_1=[[10,20,30],[4,5,6]]
matrix_2=[[5,2,3],[6,2,9]]

r=my_matrix_addition(matrix_1,matrix_2)
print(r)



#matrislerde çıkarma 
def my_matrix_substraction(m_1,m_2):
  result=[]
  for row in range (len(m_1)):
    result.append([])
    for column in range (len(m_1[0])):
      #print(m_1[row][column],end=" ")
      result[row].append(m_1[row][column]-m_2[row][column])
    #print()
  return result
matrix_1=[[10,20,30],[4,5,6]]
matrix_2=[[5,2,3],[6,2,9]]

r=my_matrix_substraction(matrix_1,matrix_2)
print(r)



#skaler çarpım
def my_matrix_scalar_product(alpha,m_1):
  result=[]
  for row in range (len(m_1)):
    result.append([])
    for column in range (len(m_1[0])):
      #print(m_1[row][column],end=" ")
      result[row].append(m_1[row][column]*alpha)
    #print()
  return result
matrix_1=[[10,20,30],[4,5,6]]
alpha=10

r=my_matrix_scalar_product(alpha,matrix_1)
print(r)



#matrislerin çarpımı
def f_1(matrix_1,i):
  return matrix_1[i]

def f_2(matrix_1,j):
  my_j_th_col=[]
  for row in matrix_1:
    for indis in range(len(row)):
      if(indis==j):
        my_j_th_col.append(row[indis])
  return my_j_th_col
matrix_1=[[4,6,3],[3,5,6]]
f_2(matrix_1,2)

matrix_1=[[4,6,3],[8,5,6]]
f_1(matrix_1,1)



def my_Vectors_Inner_Product(v,w):
  size=len(v) 
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]*w[i]

  t=0
  for i in range (size):
    t=t+my_result[i]
  return t 



def my_matrix_multiply(m_1,m_2):
  result=[]
  for row in range (len(m_1)):
    result.append([])
    for column in range (len(m_2[0])):
      #print(m_1[row][column],end=" ")
      a=f_1(m_1,row)
      b=f_2(m_2,column)
      c=my_Vectors_Inner_Product(a,b)
      result[row].append(c)
    #print()
  return result
    print(my_matrix_multiply(matrix_1,matrix_2))

matrix_1=[[10,20,30],[4,5,6]]
matrix_2=[[17,20,9],[2,7,6]




