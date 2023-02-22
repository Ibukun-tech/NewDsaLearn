# time coplexityis o(n) and space complexity is o(n)

def wordPattern(s, l):
  st=''
  for i in range(l):
    for j in range(l[i]):
      st+=l[j]
  if len(s) != len(st):
    return False
  
  charToWord={}
  wordTChar={}

  for i, j in zip(s,st):
    if i in charToWord and charToWord[i]!=j:
      return False 
    if j in wordTChar and wordTChar[j]!=i:
      return False

  return True
