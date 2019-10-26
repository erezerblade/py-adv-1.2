import json


class WikiLinkMaker:

    def __init__(self):
        self.countries = iter(self.get_counties())
        self.pair = []

    def __iter__(self):
        return self

    def __next__(self):
        country = self.countries.__next__()
        self.pair = f'{country} - https://ru.wikipedia.org/wiki/{country.replace(" ", "_")}\n'
        return self.pair

    def get_counties(self):
        with open('countries.json', encoding="utf-8") as data:
            country_list = []
            json_data = json.load(data)
            for country in json_data:
                country_list += country['translations']['rus']['common'].split('%')
        return country_list

    def store_pairs(self):
        with open('country pairs.txt', "a", encoding='utf-8') as f:
            f.write(str(self.pair))


if __name__ == "__main__":
    bublya = WikiLinkMaker()
    for pair in bublya:
        bublya.store_pairs()