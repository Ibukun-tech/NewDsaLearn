# time complexity of o(n) and space complexity of o(1)
def greaterNextElement(arr):
  input = -1
  for i in range(len(arr),-1,-1):
    maxValue =max(input, arr[i])
    arr[i]=input
    input=maxValue