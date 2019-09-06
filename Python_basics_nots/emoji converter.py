def emoji_converter(message):

    emojis = {
        ":)": "smile",
        ":(": "sad"
    }
    words = message.split(' ')
    output = ""

    for word in words:
        output += emojis.get(word , word) + ' '
    return output

message = input("> ")
print(emoji_converter(message))