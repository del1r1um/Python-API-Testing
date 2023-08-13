import requests

base_url = 'https://api.pokemonbattle.me:9104'

headers = {
    'trainer_token': 'd877b574f98f2a2a6b99dc61d93933d2',
    'Content-Type': 'application/json'
}

create_pokemon = requests.post(f'{base_url}/pokemons',
                               headers=headers,
                               json={
                                   "name": "Baby Fark XX",
                                   "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                               })
print(create_pokemon.json())

pokemon_id = requests.get(f'{base_url}/pokemons', params={'trainer_id': 1402}).json()[0]['id']
print(f'ID покемона:', pokemon_id)

change_pokemon_name = requests.put(f'{base_url}/pokemons',
                                   headers=headers,
                                   json={
                                       "pokemon_id": pokemon_id,
                                       "name": "Baby Fark XIXI",
                                       "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                                   })
print(change_pokemon_name.json())

catch_to_pokeball = requests.post(f'{base_url}/trainers/add_pokeball',
                                  headers=headers,
                                  json={'pokemon_id': pokemon_id})
print(catch_to_pokeball.json())
