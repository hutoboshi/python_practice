i = 1
i = 2

def f(arg = i):
  i = 4
  i = 5
  print(arg)
  
f()
print(i)