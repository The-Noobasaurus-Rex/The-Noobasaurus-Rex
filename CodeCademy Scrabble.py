letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
player_to_points = {}
player_to_words = {}
player_to_words["player1"] = ["blue", "tennis", "exit"]
player_to_words["wordNerd"] = ["earth", "eyes", "machine"]
player_to_words["Lexi Con"] = ["eraser", "belly", "husky"]
player_to_words["Prof Reader"] = ["zap", "coma", "period"]

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

def play_word(player, word):
  if player_to_words.get(player) != None:
    player_to_words[player].append(word)
  else:
    print("Player name: '{}' is invalid".format(player), "\n")

update_point_totals()
print(player_to_points, "\n")
