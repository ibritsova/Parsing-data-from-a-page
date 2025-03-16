import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
class ProspektParser:
    BASE_URL = "https://www.prospektmaschine.de/hypermarkte/"
    def __init__(self):
        self.flyers = []

    def fetch_html(self):
        response = requests.get(self.BASE_URL, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text

    def parse_flyers(self, html):
        soup = BeautifulSoup(html, "html.parser")
        flyer_cards = soup.find_all("div", class_="brochure-thumb")

        print(f"Nájdených {len(flyer_cards)} letákov na stránke.")  # ✅ DEBUG výstup
        i = 0
        for card in flyer_cards:
            try:
                i += 1
                title = card.find("p", class_="grid-item-content").text.strip()
                print({title})
                if i < 5:
                    thumbnail = card.find("img")["src"]
                    print({thumbnail})
                else:
                    thumbnail = card.find("img")["data-src"]
                    print({thumbnail})

                #shop_name = card.find("img")["alt"].text.strip()

                #date_range = card.find("small", class_="hidden-sm").text.strip()
                #valid_from, valid_to = self.parse_dates(date_range)

                #flyer = Flyer(title, thumbnail, shop_name, valid_from, valid_to)
                #self.flyers.append(flyer)
            except AttributeError:
                continue  

    @staticmethod
    def parse_dates(date_range):
        try:
            date_parts = date_range.split(" - ")
            valid_from = datetime.strptime(date_parts[0], "%d.%m.%Y").strftime("%Y-%m-%d")
            valid_to = datetime.strptime(date_parts[1], "%d.%m.%Y").strftime("%Y-%m-%d")
            return valid_from, valid_to
        except (IndexError, ValueError):
            return "Unknown", "Unknown"

    def save_to_json(self, filename="flyers.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([flyer.to_dict() for flyer in self.flyers], f, ensure_ascii=False, indent=4)

    def run(self):
        html = self.fetch_html()
        self.parse_flyers(html)
        self.save_to_json()
        print(f"{len(self.flyers)} letákov bolo úspešne uložených do flyers.json.")

if __name__ == "__main__":
    parser = ProspektParser()
    parser.run()