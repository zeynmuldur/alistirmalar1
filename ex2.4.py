def fibo(i):
  if i==0:
     return 0
  elif i==1:
     return 1
  else:
      return fibo(i-1)+fibo(i-2)

for i in range(1,31) :
    print(fibo(i),end=" ")
     
