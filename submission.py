import numpy as np

def count_window(grid, player, window_size):

  num_windows = 0

  ## horizontal search
  for row in range(grid.shape[0]):
    for col in range(grid.shape[1] - 3):

      grid_slice = grid[row, col:col+4]

      if np.count_nonzero(grid_slice == player) == window_size:

        if np.all(grid_slice[np.where(grid_slice != player)[0]] == 0):
          num_windows+= 1



  ## vertical search
  for col in range(grid.shape[1]):
    for row in range(grid.shape[0] - 3):
      grid_slice = grid[row:row+4, col]
      
      if np.count_nonzero(grid_slice == player) == window_size:
         
         if np.all(grid_slice[np.where(grid_slice != player)[0]] == 0):
          num_windows+= 1


  ## diagonal search
  for row in range(grid.shape[0] - 3):
    for col in range(grid.shape[1] - 3):
      window = np.diagonal(grid[row:row+4, col:col+4])
      if np.count_nonzero(window == player) == window_size:

         if np.all(window[np.where(window != player)[0]] == 0):
            num_windows+= 1

  # negative diagonal search
  for row in range(3, grid.shape[0]):
    for col in range(grid.shape[1] - 3):
      window = np.diagonal(np.fliplr(grid[row-3:row+1, col:col+4]))
      if np.count_nonzero(window == player) == window_size:

        if np.all(window[np.where(window != player)[0]] == 0):
          num_windows+= 1


  return num_windows
def score_move(grid, col_index, player):


  ## Finding Target Position
  target_position = np.where(grid[:, col_index] == 0)[0]
  target_position = max(target_position)

  ## Filling Target Position
  updated_grid = grid.copy()
  updated_grid[target_position, col_index] = player


  ## counting windows
  threes = count_window(updated_grid, player, 3)
  fours = count_window(updated_grid, player, 4)

  opp_threes = count_window(updated_grid, player%2+1, 3)


  score = (fours * 1000) - (opp_threes * 100) + threes

  return score
def my_agent(observation, configuration):

  rows = configuration.rows
  columns = configuration.columns

  inarow = configuration.inarow

  board = observation.board
  player = observation.mark

  ## convert board to 2D grid
  grid = np.asarray(board).reshape(rows, columns)

  ## list of all possible choices
  choices = [c for c in range(columns) if board[c] == 0]

  ## scoring all possible choices
  scores = [score_move(grid, col_index, player) for col_index in choices]
  print(scores)


  ## finding best choice

  return choices[np.argmax(scores)]
def count_window(grid, player, window_size):

  num_windows = 0

  ## horizontal search
  for row in range(grid.shape[0]):
    for col in range(grid.shape[1] - 3):

      grid_slice = grid[row, col:col+4]

      if np.count_nonzero(grid_slice == player) == window_size:

        if np.all(grid_slice[np.where(grid_slice != player)[0]] == 0):
          num_windows+= 1



  ## vertical search
  for col in range(grid.shape[1]):
    for row in range(grid.shape[0] - 3):
      grid_slice = grid[row:row+4, col]
      
      if np.count_nonzero(grid_slice == player) == window_size:
         
         if np.all(grid_slice[np.where(grid_slice != player)[0]] == 0):
          num_windows+= 1


  ## diagonal search
  for row in range(grid.shape[0] - 3):
    for col in range(grid.shape[1] - 3):
      window = np.diagonal(grid[row:row+4, col:col+4])
      if np.count_nonzero(window == player) == window_size:

         if np.all(window[np.where(window != player)[0]] == 0):
            num_windows+= 1

  # negative diagonal search
  for row in range(3, grid.shape[0]):
    for col in range(grid.shape[1] - 3):
      window = np.diagonal(np.fliplr(grid[row-3:row+1, col:col+4]))
      if np.count_nonzero(window == player) == window_size:

        if np.all(window[np.where(window != player)[0]] == 0):
          num_windows+= 1


  return num_windows
def score_move(grid, col_index, player):


  ## Finding Target Position
  target_position = np.where(grid[:, col_index] == 0)[0]
  target_position = max(target_position)

  ## Filling Target Position
  updated_grid = grid.copy()
  updated_grid[target_position, col_index] = player


  ## counting windows
  threes = count_window(updated_grid, player, 3)
  fours = count_window(updated_grid, player, 4)

  opp_threes = count_window(updated_grid, player%2+1, 3)


  score = (fours * 1000) - (opp_threes * 100) + threes

  return score
def my_agent(observation, configuration):

  rows = configuration.rows
  columns = configuration.columns

  inarow = configuration.inarow

  board = observation.board
  player = observation.mark

  ## convert board to 2D grid
  grid = np.asarray(board).reshape(rows, columns)

  ## list of all possible choices
  choices = [c for c in range(columns) if board[c] == 0]

  ## scoring all possible choices
  scores = [score_move(grid, col_index, player) for col_index in choices]
  print(scores)


  ## finding best choice

  return choices[np.argmax(scores)]
