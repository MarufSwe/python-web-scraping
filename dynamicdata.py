import csv
from requests_html import HTMLSession


url = 'https://www.beerwulf.com/en-gb/c/beers?segment=Beers&catalogCode=Beer_1'

s = HTMLSession()
r = s.get(url)

# r.html.render(sleep=1)

products = r.html.xpath('//*[@id="product-items-container"]', first=True)

for item in products:
    print(item)