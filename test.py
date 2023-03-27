import pprint
import json
from requests import get, post, delete, put

# ff = open('response.json')
# Response: Говорит Алиса.
# pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json())
# ff.close()

ff = open('request.json', encoding='utf8')
pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json()['response']['text'])
ff.close()
print()

ff = open('req_vasya.json', encoding='utf8')
pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json()['response']['text'])
ff.close()
print()

ff = open('req_paris.json', encoding='utf8')
pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json()['response'])
ff.close()
print()

ff = open('req_moscow.json', encoding='utf8')
pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json()['response'])
ff.close()
print()


