# python3

import sys
import numpy

input = sys.stdin.read()
tokens = input.split()

def findmax(tokens):
  max_value = 0
  location = 0
  for i in range(1,len(tokens)):
    x = int(tokens[i])
    if max_value < x:
      max_value = x
      location = i
    else:
      max_value = max_value
  return (location, max_value)


def max_pairwise_product(data):
  max_1 = findmax(data)
  del data[max_1[0]]
  max_2 = findmax(data)
  return (max_1[1] * max_2[1])



print (max_pairwise_product(tokens))