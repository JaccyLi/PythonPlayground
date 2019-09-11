# Use your Python dictionary skills to keep point totals for 4 people playing a game of scrabble!
# Say goodbye to the pencil-and-notebook scoring method of the past.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters +=[
  letter.lower()
  for letter
  in letters
]

points *= 2
# print(letters)
# print(points)

# map letter with points
letter_to_points = {
    letter: point
    for letter, point
    in zip(letters, points)
}
# print(letter_to_points)

letter_to_points[""] = 0
# print(letter_to_points)


def score_word(word):
    point_total = 0
    for w in word:
        point_total += letter_to_points.get(w, 0)
    return point_total


brownie_points = score_word("DD")
print(brownie_points)


player_to_words = {"player1": ['BLUE', 'TENNIS', 'EXIT'],
                   "wordNerd": ['EARTH', 'EYES', "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader": ["zap", "coma", "period"]
}

player_to_points = {}


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


update_point_totals()
print(player_to_points)


def play_word(player, word):
    player_to_words[player].append(word)


play_word("player1", "jHK")
print(player_to_words)
