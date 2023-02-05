# space complexity of o(n) and time complexity of o(n)

def uniqueEmails(emails):
  val=set()
  for e in emails:
    i, local=0,''
    while e[i] not in ['@', '+']:
      local+=e[i]
      if e[i] == '.':
        local+=e[i]
      i+=1
    while e[i] != '@':
      i+=1
      domain=e[i+1:]
    
    val.add((local, domain))

  return len(val)