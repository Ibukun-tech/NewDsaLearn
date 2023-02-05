# space complexity of o(n) and time complexity of o(n)

def pascalsTriangle(value):
  res=[[1]]
  for j in range(value-1):
    vals=[0]+res[-1]+[0]
    temp=[]
    for j in range(len(vals)+1):
      temp.append(vals[j]+vals[j+1])
    res.append(temp)
    return res
