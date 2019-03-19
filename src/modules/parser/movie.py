class Movie(object):
    def __init__(self, title, href, year, quality, rating, genre):
        self.title = title
        self.href = href
        self.year = year
        self.quality = quality
        self.rating = rating
        self.genre = genre

    def as_list(self):
        return [self.title, self.year, self.quality, self.rating, self.genre]