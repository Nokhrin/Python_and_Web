"""
Даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получить информацию
о имени художника и годе рождения.

Вывести имена художников
в порядке неубывания года рождения.
В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.
"""


"""
API
https://developers.artsy.net/
Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret. 
Не публикуйте эти идентификаторы.
"""

"""
Input Example
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Output Example
Abbott Mary
Warhol Andy
Abbas Hamra
"""


import json
import requests


CLIENT_ID = '0d83f6a13efe5c02de50'
CLIENT_SECRET = '130bfa39a61fbda0d0fa96e1eb968165'

# get the token
request_token = requests.post(
    url='https://api.artsy.net/api/tokens/xapp_token',
    data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
)

response_json = json.loads(request_token.text)
# print(response_json)
token = response_json['token']

def get_artist_data(id):
    """get json with artist's data"""
    BASE_URL = f'https://api.artsy.net/api/artists/{id}'
    # header
    headers = {
        'Content-Type': 'application/json',
        'X-Xapp-Token': token
    }
    # request
    response = requests.get(url=BASE_URL, headers=headers)
    response.encoding = 'utf-8'
    response_json = json.loads(response.text)
    # artist's name: sortable_name in UTF-8
    name = response_json['sortable_name']
    birthday = response_json['birthday']
    return f'{birthday} {name}'


INPUT_FILENAME = 'artists_input.txt'
OUTPUT_FILENAME = 'artists by birth year.txt'
with open(INPUT_FILENAME, 'r', encoding='utf-8', newline='') as f_input, open(OUTPUT_FILENAME, 'w', encoding='utf-8', newline='\n') as f_output:
    year_name_list = []
    for artist_id in f_input.read().splitlines():
        year_name_list.append(get_artist_data(artist_id))

    year_name_list.sort()  # sort by year, if years are equal, sort by following name
    # print(year_name_list)
    artists_list = []
    for year_name in year_name_list:
        name = year_name[5:]
        f_output.write(name + '\n')
