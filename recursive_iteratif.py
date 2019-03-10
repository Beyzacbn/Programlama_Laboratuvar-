#fibonacci iteratif
def fibonacci_loop(n):
  a,b=0,1
  for i in range (n-1):
    a,b=b,a+b
  return a

#fibonacci recursive
def fibonacci_recursive(n):
  if(n<2):
    return n
  else:
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


#birden n e kadar iteratif faktöriyel
def factorial(n):
  s=1
  for i in range(n):
    s=s*i
  return s
#birden n e kadar recursive faktöriyel
def factorial_recursive(n):
  if(n==1):
    return n
  else:
    return n*factorial_recursive(n-1)


#üs hesaplama iteratif
def power(m,n): #m üzeri n lineer gibiyse
  s=m
  for i in range(1,n):
    s=s*m
  return s

#üs hesaplama recursive
def power_recursive(m,n):   #binary search gibi
  if(n==0):
    return 1
  elif(n==1):
    return m
  elif(n/2==0):
    return power_recursive(m*m,n/2)
  elif(n//2!=0):
    return power_recursive(m*m,n/2)

  for i in range(10):
    r_1=fibonacci_loop(i)
    r_2=fibonacci_loop(i)
    print("fibonacci_loop: ",r_1 , end=" ")
    print("fibonacci_recursive: ",r_2,end=" ")


