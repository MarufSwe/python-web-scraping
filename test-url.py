from requests_html import HTMLSession

# url = 'https://stackoverflow.com/questions/tagged/javascript?tab=votes&pagesize=50'
url = 'https://stackoverflow.com/questions/tagged/javascript?tab=votes&page=2&pagesize=50'

s = HTMLSession()
r = s.get(url)

# r.html.render(sleep=1)

# questions = r.html.xpath('//*[@id="questions"]' , first=True)
questions = r.html.xpath('//*[@id="mainbar"]' , first=True)

# print(questions.absolute_links)

for item in questions.absolute_links:
    r = s.get(item)
    headline = r.html.find('.question-hyperlink', first=True).text  # Question Headline HTML class id
    print(headline)