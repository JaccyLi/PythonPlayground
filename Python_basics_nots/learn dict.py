songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

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

