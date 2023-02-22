# time complexity of o(n) and space complexity of o(n)

def numberOfBallons(chr):
  countText=Counter(chr)
  counBallon=Counter('ballon')
  res=len(countBallon)
  for n in counBallon:
    res= min(res,countText[n]//countBallon)
  return res

