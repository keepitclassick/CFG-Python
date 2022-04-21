import random

import requests


def random_card():
    # gen random number between 1 and 151
    card_id = random.randint(1, 151)
    # input the random number as an 'id' in the pokemon API request
    req_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(card_id)
    # send the request
    res = requests.get(req_url)
    # convert response to JSON
    card_details = res.json()

    return {
        'name': card_details['name'],
        'id': card_details['id'],
        'height': card_details['height'],
        'weight': card_details['weight'],
    }


def play():
    # gen random cards for both the player and the opponent
    player_card = random_card()
    opponent_card = random_card()

    # show player which card they have drawn
    print('{}, I choose you!'.format(player_card['name']))
    # player chooses which stat to use for the fight
    stat_choice = input('Will you use {}\'s id, height or weight to fight?'.format(player_card['name']))

    print('The opponent has chosen {}'.format(opponent_card['name']))

    player_stat = player_card[stat_choice]
    opponent_stat = opponent_card[stat_choice]

    if player_stat > opponent_stat:
        print('Victory is yours!')
    elif player_stat < opponent_stat:
        print('You\'ll get \'em next time!')
    else:
        print('It\'s a tie!')


play()


