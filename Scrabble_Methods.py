letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ""]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letters_to_points = {letters:points for letters, points in zip(letters, points)}

users = []

def user_input(user):
    users.append(user)
    return user

def score_word(word):
  point_total = 0
  for letters in word.upper():
      point_total += letters_to_points.get(letters, 0)
  return point_total

def total_points(players):
    player_to_points = {}
    for player, words in players.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    print("Punktestand: ", player_to_points)
    return player_to_points

def play_word(player, word):
  print("{} hat das Wort {} gespielt!".format(player, word))
  empty_list = []
  if player in players.keys():
    empty_list = (players.get(player))
    empty_list.append(word.upper())
    players.update({player: empty_list})
  else:
    players.update({player: word})
  points = total_points()
  points = points.get(player)
  print("Neue Punktzahl des spielers: {} ist: {}".format(player, points))
  return players
