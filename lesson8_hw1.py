# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.
# Задача №1. Написать программу для файла в формате json.

import json
from pprint import pprint
from collections import Counter


def getting_text_from_json(filename):
    """ Opening file anf reading data to news_text"""
    with open(filename, encoding="utf-8") as read_file:
        json_data = json.load(read_file)
    items = json_data["rss"]["channel"]["items"]
    news_text = ''
    for item in items:
        news_text += item["description"]
    return news_text


def rating_news_text(news_text, char_count, word_count):
    """ Creating top list of words """
    words = news_text.split()
    filter_list = []
    res = []
    for word in words:
        if len(word) >= int(char_count):
            filter_list.append(word)
    low_words = [word.lower() for word in filter_list]
    word_counts = Counter(low_words).most_common(int(word_count))
    return word_counts


def main():
    pprint(rating_news_text(getting_text_from_json(
        "newsafr.json"), input("Кол-во символов: "), input("кол-во слов: ")))


main()
