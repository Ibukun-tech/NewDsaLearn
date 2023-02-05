# space complexity of o(n) and time copmlexity of o(n)

def groupOfAnagrams(str):
  hashMap=defauldict(list)
  for s in str:
    count=[0]*26
    for i in s:
      count[ord(i)-ord('a')]+1
    hashMap(tuple(count)).append(s)
  
  return hashMap.Values()