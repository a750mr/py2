import json

import requests

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

json_in = json.loads(json_text)

json_list = json_in['messages']

print(json_in['messages'][1])
