# Time complexity of o(n) and a space complexity of o(n)

def canReplaceFlowers(arr, val):
  newArr=[0]+arr+[0]

  for i in range(1,len(newArr)-1):
    if newArr[i]==0 and newArr[i+1]==0 and newArr[i-1]==0:
      newArr[i]=1
      val-=1
  return val <=0