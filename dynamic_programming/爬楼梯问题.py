a = 1
b = 2
temp = 0

def upstairs(n):
  if n < 1:
    print(0)
  if n == 1:
    print(1)
  if n == 2:
    print(2)
  
  a = 1
  b = 2
  temp = 0

  for i in range(2, n):
    temp = a + b
    a = b
    b = temp
    #a, b = b, a + b
    #b, a= a + b, b
  print(temp)

upstairs(10)
89
