songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
# list comprehension
plays = {song:count for song, count in zip(songs, playcounts)}
print(plays)
plays['Purple Haze'] = 1
plays['Respect'] = plays['Respect'] + 5
print(plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)


customer = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
phone = input("Phone number:")
for num in phone:
    output += customer.get(num , " !") + " "
print(output)

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13, "none")

print(spread)

spread["present"] = tarot.pop(22, "none")
print(spread)

spread["future"] = tarot.pop(10, "none")
print(spread)

for k, v in spread.items():
  print(f"Your {k} is the {v} card.")