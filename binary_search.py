# python3
import sys

input = sys.stdin.read()
tokens = input.splitlines()
sorted_array = tokens[0].split()
keywords = tokens[1].split()

n = int(sorted_array[0])
a_temp = sorted_array[1:]
a = [int(number) for number in a_temp]

k = int(keywords[0])
b_temp = keywords[1:]
b = [int(number) for number in b_temp]

def binary_search(a, indices, key):
  rslt = -1
  l = len(a)
  while l > 0:
    if l%2 == 1:
      index = l//2
      temp = a[index]
      if key == temp:
        rslt = indices[index]
        l = 0
      elif key < temp:
        a = a[:index]
        l = len(a)
        indices = indices[:index]
      else:
        a = a[(index+1):]
        l = len(a)
        indices = indices[(index+1):]
    else:
      index = [int(l/2)-1, int(l/2)]
      temp = (a[index[0]] + a[index[1]])/2
      if key == temp:
        rslt = [indices[index[0]], indices[index[1]]]
        l = 0
      elif key < temp:
        a = a[:(index[0]+1)]
        l = len(a)
        indices = indices[:(index[0]+1)]
      else:
        a = a[index[1]:]
        l = len(a)
        indices = indices[index[1]:]
  return rslt


# a = [1,2,3,4,5]
# n = 5

# b = [0,2]
# k = 2
results = []
for i in range(0,len(b)):
  print (binary_search(a, indices=range(0,len(a)), key=b[i]), end=' ')




