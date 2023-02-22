# this will take a time complexity of o(9*9) and a space complexity of o(n)


def isValidSudoku(board):
  cols=Collections.defaultdict(set)
  rows=Collections.defaultdict(set)
  squares=Collections.defaultdict(set)

  for r in range(9):
    for c in range(9):
      if board[r][c] =='.':
        continue
      if (board[r][c] in cols[c] or 
      board[r][c] in rows[r] or 
      board[c][r] in squares(c/3,r/3)):
        return False
      cols[c].add(board[r][c])
      rows[r].add(board[r][c])
      squares[c/3,r/3].add(board[r][c])
  
  return True