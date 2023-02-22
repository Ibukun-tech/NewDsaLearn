# this will haave a time complexity of o(n) and a space complexity of o(n)

def productExceptItself(arr):
  res=[-1]*len(arr)

  prefix=1
  for i in range(len(arr)):
    res[i]=prefix 
    prefix*=arr[i]
  postFix=1
  for i in range(len(arr), -1, -1):
    res[i]*=postFix
    postFix*=arr[i]
  return res