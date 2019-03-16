# from modules.parser import movie
import re
import requests
from lxml import etree
from io import StringIO
from prettytable import PrettyTable

from movie import Movie

SHOW_GENRE = False

# _searchparam = input('Search: ')
_searchparam = 'spider'
r = requests.get('https://genvideos.co/results?q=' + _searchparam)

parser = etree.HTMLParser()
tree = etree.parse(StringIO(r.text), parser)

_movies = []
_elements = []
_list = tree.findall('.//div')
for x in _list:
    if x.attrib.get('class') == 'cell':
        _elements.append(x)

for ele in _elements:
    a = ele.find('.//a')
    _title = a.get('title')
    _href = a.get('href')

    _parts = ele.findall('.//b')
    _year = re.findall(r'\d+', _parts[0].tail)[0]
    _quality = re.findall(r'\d+', _parts[1].tail)[0] + 'p'
    _rating = _parts[2].tail.strip()
    _genre = _parts[3].tail.strip()

    _movies.append(Movie(_title, _href, _year, _quality, _rating, _genre))

pt = PrettyTable()
if SHOW_GENRE:
    pt.field_names = ['ID', 'Title', 'Year', 'Quality', 'Rating', 'Genre']
else:
    pt.field_names = ['ID', 'Title', 'Year', 'Quality', 'Rating']
number = [0]
for movie in _movies:
    pt.add_row([*number, *movie.as_list()])

pt.reversesort = True
pt.sortby = "Rating"
print(pt)