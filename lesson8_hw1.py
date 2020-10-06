# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.
# Задача №1.
# Написать программу для файла в формате json.


import json
import re
from collections import Counter


def get_text_from_json():
    with open("newsafr.json", encoding="utf-8") as read_file:
        json_data = json.load(read_file)
    titles = json_data["rss"]["channel"]["items"]
    descriptions_text = ''
    for title in titles:
        descriptions_text += title["description"]
    return descriptions_text


def text_filtering(descriptions_text, word_count):
    text_string = descriptions_text.lower()
    match_pattern = re.findall(r'\b[а-я,a-z]{6,100}\b', text_string)
    return Counter(match_pattern).most_common(word_count)


def main():
    get_text_from_json()
    print(text_filtering(get_text_from_json(), int(input('кол-во слов: ')))  )


main()
