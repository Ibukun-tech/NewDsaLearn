# time complexity is o(n) and space complexity is o(n)

def topKFrequentElement(arr,val):
  count={}
  res=[]
  freq=[[]]*len(arr)+1
  for n in arr:
    count[n]=1+count.get(n,0)
  for n, c in count.items():
    freq[c].append(n)
  for i in range(len(freq),0,-1):
    for n in freq[i]:
      res.append(n)
      if len(res)==val:
        return res
