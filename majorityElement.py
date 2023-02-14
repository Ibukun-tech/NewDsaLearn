# time complexity of o(n) and space complexity of o(n)
def majorityElement(arr):
  hashIndex={}
  res, maxCount=0,0
  for n in nums:
    hashIndex[n]=1+hashIndex.get(n,0)
    if hashIndex[n] > maxCount:
      res=n
      maxCount=max(maxCount, hashIndex[n])
  return res

# This is the boyer moore algorithm which has a time coplexity of o(n ) and a space complexity of o(1)

def majorityElemeent(arr):
  count,res=0,0
  for i in range(len(arr)):
    if count == 0:
      res=arr[i]
    if res == arr[i]:
      count+=1
    else:
      count-=1
  return res
