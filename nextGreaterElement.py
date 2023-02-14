# space complexity of o(atr2*arr2 + arr1) and time complexity of o(n)

def nextGreaterElement(arr1, arr2):
  newArr1=[-1]* len(arr1)
  hashIndex={}
  for i , j in enumerate(arr1):
    hashIndex[j]=i
  for j in range(arr2):
    if arr2[j] not in hashIndex:
      continue
    for i in range(j+1, arr2):
      if arr2[i] > arr[j]:
        val=hashIndex[j]
        newArr1[val]=arr2[i]
    break
  return newArr1

# or we can have the one in which we can have time of o(n) and 

def nextGreaterElement(arr1, arr2):
  newArr=[-1] * len(arr1)
  hashIndex={}
  for i,j in enumerate(arr1):
    hashIndex[j]=i
  stack=[]
  for j in range(arr2):
    val=arr2[j]
    while stack and val>stack[-1]:
      replaceValue=stack.pop()
      indexOfReplaceValue=hashIndex[newAppend]
      newArr[indexOfReplaceValue]=val

      if val in hashIndex:
        stack.append(val)
  return newArr


