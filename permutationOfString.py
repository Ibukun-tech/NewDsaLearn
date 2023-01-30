# time complexity of o(n) and space complexity of o(n)

def permutationOfString(s,t):
  countS, countT={}, {}

  for c in range(len(s)):
    countS[s[c]]= 1+countS.get(s[c], 0)
    countT[t[c]]=1+countT.get(t[c], 0)
  for s in countS:
    if countS[s] !=countT[s].get(s,0):
      return False
  
  return True

# time complexity of o(tlogt)
def permutationOfString(s,t):
  return s == t.sort()