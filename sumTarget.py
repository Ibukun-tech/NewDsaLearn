def indexesOfTwoNum(arr,i):
  curr={}
  for j, i in enumerate(len(arr)):
    r=i-arr[i]
    if r in curr:
      return [curr[r],i]
    curr[j]=i