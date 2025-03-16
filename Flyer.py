from datetime import datetime


class Flyer:
    def __init__(self, title, thumbnail, shop_name, valid_from, valid_to):
        self.title = title
        self.thumbnail = thumbnail
        self.shop_name = shop_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def to_dict(self):
        return {
            "title": self.title,
            "thumbnail": self.thumbnail,
            "shop_name": self.shop_name,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "parsed_time": self.parsed_time
        }