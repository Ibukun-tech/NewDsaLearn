# Time complexity is o(n) and space complexity is o(1)

def longestCommonPrefix(s):
  st=s[0]
  res=''
  for i in range(len(st)):
    for j in s:
      if st[i]!=j[i]:
        return res
      res+=st[i]
  return res
    