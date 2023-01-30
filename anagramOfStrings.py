#  time complexity of o(n) and space complexit of o(n)
def anagramOfStrings(s,t):
  countS, countT={},{}

  for i in range(len(s)):
    countS[s[i]]=1 + countS.get(s[i], 0)
    countT[t[i]]=1 + countT.get(t[i], 0)
  for c in s:
    return countS[c] == countT.get(c,0)