import csv
from requests_html import HTML, HTMLSession

csv_file = open('cms.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'body', 'video'])

session = HTMLSession()
res = session.get('https://coreyms.com')

articles = res.html.find('article')

for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print("Headline:", headline)

    body = article.find('.entry-content p', first=True).text
    print("Body:", body)

    try:
        video_src = article.find('iframe', first=True).attrs['src']
        video_id = video_src.split('/')[4]  # id is in 4rth index of youtube link
        video_id = video_id.split('?')[0]  # before '?' is video id, and after '?' is video parameters
        # print("Video:", video_id)
        yt_link = f'https://www.youtube.com/watch?v={video_id}'
    except Exception as e:
        yt_link = None

    print("Video:", yt_link)
    print()

    csv_writer.writerow([headline, body, yt_link])

csv_file.close()

