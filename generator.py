import json
import hashlib


def generate_pairs(path):
    country_list = []
    with open(path, encoding="utf-8") as data:
        json_data = json.load(data)
        for country in json_data:
            country_list += country['translations']['rus']['common'].split('%')
    countries = iter(country_list)
    counter = 0
    while counter < 250:
        country = countries.__next__()
        pair = f'{country} - https://ru.wikipedia.org/wiki/{country.replace(" ", "_")}\n'
        with open('country pairs.txt', "a", encoding='utf-8') as f:
            f.write(str(pair))
        counter +=1
        yield pair


if __name__ == "__main__":
    for pair in generate_pairs('countries.json'):
        print(hashlib.md5(pair.encode('utf-8')).hexdigest())
