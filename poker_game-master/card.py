import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
url1 = "https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"

url2 = "https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"

response = requests.get(url)
cards_dict = json.loads(response.text)

#if (cards_dict['success'] & cards_dict['shuffled']):
    
suits = {"SPADES": "♠️","CLUBS": "♣️", "HEARTS": "♥️","DIAMONDS": "♦️"}

n =int (input())

card_of_user = [[""]*2]*(n+1)

for i in range (1,n+1):
    
    response1 = requests.get(url1.format(deck_id=cards_dict['deck_id']))
    cards_dict_main = json.loads(response1.text)

    for j in range(0,2):
 
        suit = cards_dict_main['cards'][j]['suit']

        card_of_user[i][j] = cards_dict_main['cards'][j]['value'][0] + suits[suit]


    print(*card_of_user[i])


cards_on_table = [""]*6

response1 = requests.get(url2.format(deck_id=cards_dict['deck_id']))
cards_dict_main = json.loads(response1.text)

for j in range(0,5):
 
    suit = cards_dict_main['cards'][j]['suit']

    cards_on_table[j] = cards_dict_main['cards'][j]['value'][0] + suits[suit]


print(*cards_on_table)





"""
♠️ ♣️ ♥️ ♦️
poker
запрос
массив(n=кол-ву игроков)
стол
n = 4
i=1
    1 раз получаем json
    получаем коды карт
    запоминаем в массив
i=2
    2 раз получаем json
    получаем коды карт
    запоминаем в массив
ш=3
ш=4
по 2 карты
5 карт для всех
2 2 2 2 2
    "Роял флэш" - наивысшая комбинация в покере, пять карт от десятки до туза одной масти.
    "Стрит флэш" - пять последовательных карт одной масти.
    "Каре" - четыре карты одного достоинства.
    "Фул хаус" - включает в себя три карты одного достоинства и две - другого достоинства.
    "Флэш" – любые пять карт одной масти.
    "Стрит" - пять последовательных карт.
    "Тройка" - три карты одного достоинства.
    "Две пары" - две карты одного достоинства и две другого достоинства.
    "Пара" - пара из двух карт одного достоинства.
    "Старшая карта или киккер" - выигрывает рука с наивысшей картой.
"""