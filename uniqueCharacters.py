# Time complexity o(n) space complexity is o(n)
def uniqueCharacter(str):
  return len(str) == set(str)

#  Time complexity of o(n*n) and space complexity of o(1)
def uniqueCharacter(str):
  for i in range(len(str)):
    for j+i in range(len(str)):
      if str[j] == str(i):
        return True

  return False 