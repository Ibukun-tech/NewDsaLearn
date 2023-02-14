# This will have a space complexity of o(1) and a time complexity of o(n)

def pivotIndex(nums):
  total=sum(nums)
  leftSum=0
  for i in range(nums):
    rightSum=total- nums[i]-leftSum
    if rightSum==leftSum:
      return i
    leftSum+=nums[i]
  return -1