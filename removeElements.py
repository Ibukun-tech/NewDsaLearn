# space complexity of o(1) and time complexity of o(n)
def removeElements(nums, val):
  k=0
  for j in nums:
    if j != val:
      nums[k]=j
      k+=1
  return k