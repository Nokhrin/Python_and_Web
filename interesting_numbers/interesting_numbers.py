"""
Использовать API сайта numbersapi.com
Дается набор чисел.
Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
Для каждого числа вывести Interesting,
если для числа существует интересный факт,
и Boring иначе.

Выводить информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""

"""
URL Structure

Just hit http://numbersapi.com/number/type to get a plain text response, where

    type is one of trivia, math, date, or year. Defaults to trivia if omitted.
    number is
        an integer, or
        the keyword random, for which we will try to return a random available fact, or
        a day of year in the form month/day (eg. 2/29, 1/09, 04/1), if type is date
        ranges of numbers

"""

import requests


INPUT_FILENAME = 'dataset_24476_3_input.txt'
TYPE = 'math'


def get_number_info(number: str, request_type: str):
    """connect to numbersapi.com and retrieve the data"""
    URL = f'http://numbersapi.com/{number}/{request_type}?json'

    response = requests.get(URL)
    # print(response.url)
    # print(response.status_code)
    # print(response.headers['Content-Type'])  # should be application/json

    res_json = response.json()
    return bool(res_json['found'])


with open(INPUT_FILENAME, 'r', encoding='utf-8', newline='') as f_input, open('interesting_numbers_output.txt', 'w', encoding='utf-8', newline='\n') as f_output:
    for line in f_input.read().splitlines():
        NUMBER = line
        if get_number_info(NUMBER, TYPE):
            result = 'Interesting'
        else:
            result = 'Boring'
        f_output.write(result + '\n')
