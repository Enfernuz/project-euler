#python 3

def getSumOfEvenFibonacciTerms (limit):
  prevTerm = 1
  nextTerm = 2
  sum = 2
  # Starting from the term 2, each next 3rd Fibonacci term is even (indexing from 1).
  # The logic is simple: 
  #    1 (odd) + 2 (even) = 3 (odd) --> the start of the sequence: odd + even = odd, order = 1
  #    2 (even) + 3 (odd) = 5 (odd) --> even + odd = odd, order = 2
  #    3 (odd) + 5 (odd) = 8 (even) --> odd + odd = even, order = 3
  #    5 (odd) + 8 (even) = 13 (odd) --> the sequence repeats from here
  #    ...
  order = 1 
  while nextTerm <= limit:
    tmp = nextTerm
    nextTerm = prevTerm + nextTerm
    prevTerm = tmp
    if order == 3:
      sum += nextTerm
      order = 1
    else:
      order += 1
  return sum

print( getSumOfEvenFibonacciTerms(4000000) )

