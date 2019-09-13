import json

# e1
with open('../test_file/message.json') as message_json:
    message = json.load(message_json)

print(message['text'])

# e2
data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
     'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)

