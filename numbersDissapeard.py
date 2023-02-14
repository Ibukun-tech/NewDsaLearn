# Time complexity of o(n) and space complexity of o(n)

def numberDisappeared(nums):

  for n in nums:
    i =abs(n)-1
    nums[i]=-1*abs[nums[i]]

    res=[]
    for i, j in enumerate(nums):
      if j > 0:
        res.append(i+1)
    return res