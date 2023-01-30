# time complexity of o(n) and space complexity of o(1)
def lengthOfLastWord(str):
  l=len(str)
  length=0
  while l>0 and str[l]==' ':
    l-=1
  while l>0 ND str[l] != ' ':
    l-=1
    length+=1
  
  return length