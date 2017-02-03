# python3
import sys

input = sys.stdin.read()
tokens = input.split()
n_1 = int(tokens[0])
n_2 = int(tokens[1])
n_1 = abs(n_1)
n_2 = abs(n_2)

def gcd(n_1, n_2):
  if n_1 > n_2:
    a = n_1
    b = n_2
  else:
    a = n_2
    b = n_1
  r_new = a % b
  r_old = b 
  while r_new!=0:
    temp = r_new
    r_new = r_old % temp
    r_old = temp
  return r_old

print (gcd(n_1,n_2))


    
  



