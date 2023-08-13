import requests
import pytest

base_url = 'https://api.pokemonbattle.me:9104'

def test_trainers_status_code():
    response = requests.get(f'{base_url}/trainers')
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'Baby Fark McGee-zax'),
                                        ('id', '1402'),
                                        ('city', 'Moscow')])
def test_trainer_name(key, value):
    response = requests.get(f'{base_url}/trainers', params={'trainer_id': 1402})
    assert response.json()[key] == value
