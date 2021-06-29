class Solution():
  def solveSudoku(self, board):
    self.helper(board, 0)

  def helper(self, board, index):
    if index >= 81:
      self.printSolution(board)
      return
    if board[index] == 0:
      for i in range(10):
        if self.isValid(board, index, i):
          board[index] = i
          self.helper(board, index + 1)
          board[index] = 0
    else:
      self.helper(board, index + 1)
    
  def printSolution(self, board):
    for i in range(0, 81, 9):
      print(board[i : i + 9])
  
  def isValid(self, board, index, num):
    row = index // 9
    column = index % 9
    for i in range(index + 9, 81, 9):
      if board[i] == num:
        return False
    for i in range(index - 9, -1, -9):
      if board[i] == num:
        return False
    for i in range(9 * row, 9 * (row + 1)):
      if board[i] == num:
        return False
    for i in range(row - row % 3, 3 + row - row % 3):
      for j in range(column - column % 3, 3 + column - column % 3):
        if board[j + i * 9] == num:
          return False
    return True

Solution().solveSudoku(
[4,1,0,0,0,7,8,5,0,
 8,0,6,0,0,0,0,0,9,
 0,2,0,0,9,0,6,0,0,
 0,0,4,0,0,0,0,1,2,
 2,0,0,5,8,0,0,7,0,
 0,0,0,0,0,0,5,0,0,
 0,0,0,7,0,2,0,0,0,
 0,0,8,0,1,0,0,0,0,
 0,7,0,0,6,0,0,0,0]
)

output:
  [4, 1, 9, 6, 2, 7, 8, 5, 3]
  [8, 3, 6, 1, 5, 4, 7, 2, 9]
  [7, 2, 5, 3, 9, 8, 6, 4, 1]
  [5, 8, 4, 9, 7, 6, 3, 1, 2]
  [2, 9, 3, 5, 8, 1, 4, 7, 6]
  [1, 6, 7, 2, 4, 3, 5, 9, 8]
  [6, 4, 1, 7, 3, 2, 9, 8, 5]
  [3, 5, 8, 4, 1, 9, 2, 6, 7]
  [9, 7, 2, 8, 6, 5, 1, 3, 4]
