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
  twos = count_window(updated_grid, player, 2)


  opp_threes = count_window(updated_grid, player%2+1, 3)
  opp_twos = count_window(updated_grid, player%2+1, 2)


  score = (fours * 10000) - (opp_threes * 1000) + 10*threes + 1*twos - (opp_twos * 10)

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

  for c in choices:
    observation.board[c] = player
  ## scoring all possible choices - via one step lookahead
  scores = [score_move(grid, col_index, player) for col_index in choices]


  ## finding best choice
  best_score = np.max(scores)

  best_scores_index = np.where(scores == best_score)[0]

  from random import choice

  return choices[choice(best_scores_index)]
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
def score_move(grid, player):



  ## counting windows
  threes = count_window(grid, player, 3)
  fours = count_window(grid, player, 4)
  twos = count_window(grid, player, 2)


  opp_threes = count_window(grid, player%2+1, 3)
  opp_four = count_window(grid, player%2+1, 4)
  opp_twos = count_window(grid, player%2+1, 2)


  score = (fours * 1000) - (opp_threes * 1000) + 100*threes + 1*twos - (opp_twos * 10) - (opp_four*10000)

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

  ## scoring all possible choices - via one step lookahead
  scores = []
  for col_index in choices:
    scores.append(minimax(col_index, 2 ,observation, configuration, True, grid))
    grid = np.asarray(board).reshape(rows, columns)

  
  print(scores)

 


  ## finding best choice
  best_score = np.max(scores)

  best_scores_index = np.where(scores == best_score)[0]

  from random import choice

  return choices[choice(best_scores_index)]
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
def score_move(grid, player):



  ## counting windows
  threes = count_window(grid, player, 3)
  fours = count_window(grid, player, 4)
  twos = count_window(grid, player, 2)


  opp_threes = count_window(grid, player%2+1, 3)
  opp_four = count_window(grid, player%2+1, 4)
  opp_twos = count_window(grid, player%2+1, 2)


  score = (fours * 1000) - (opp_threes * 1000) + 100*threes + 1*twos - (opp_twos * 10) - (opp_four*10000)

  return score
def minimax(grid, col_index, depth, maximizingPlayer, player, configuration): 
    # Check if column is valid
    if grid[0,col_index] != 0:
        return np.inf if maximizingPlayer else -np.inf

    # Drop piece in the column
    row = np.where(grid[:, col_index] == 0)[0][-1]
    grid[row,col_index] = player

    # Check for terminal state or max depth
    if count_window(grid, player, configuration.inarow) > 0:
        return 10000 if maximizingPlayer else -10000
    if count_window(grid, player%2+1, configuration.inarow) > 0:
        return -10000 if maximizingPlayer else 10000
    if depth == 0 or np.all(grid != 0):
        return score_move(grid, observation.mark)

    # Recursive minimax calls
    if maximizingPlayer:
        max_score = -np.inf
        for c in range(configuration.columns):
            score = minimax(grid.copy(), c, depth - 1, False, 3 - player, configuration)
            max_score = max(max_score, score)
        return max_score
    else:
        min_score = np.inf
        for c in range(configuration.columns):
            score = minimax(grid.copy(), c, depth - 1, True, 3 - player, configuration)
            min_score = min(min_score, score)
        return min_score
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

  ## scoring all possible choices - via one step lookahead
  scores = []
  for col_index in choices:
    scores.append(minimax(grid.copy(), col_index, 3, True, observation.mark, configuration))


  ## return best choice
  return choices[np.argmax(scores)] 
