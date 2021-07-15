import csv
from requests_html import HTML, HTMLSession
session = HTMLSession()


# File Save as CSV Format
csv_file = open('questions_body.csv', 'w') #save file name
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Questions', 'Body', 'Tags']) #column name

session = HTMLSession()
res = session.get('https://stackoverflow.com/questions/tagged/javascript?tab=votes&pagesize=50') #link

questions = res.html.find('.summary') #HTML parent id (by '.' catch the html class)

for summary in questions:
    headline = summary.find('.question-hyperlink', first=True).text  #Question Headline HTML class id
    print("Headline:", headline)

    body = summary.find('.excerpt', first=True).text  #Question Body HTML class id
    print("Body:", body)


    # body_details = summary.find('.js-post-body', first=True).text  # Question Body HTML class id
    # print("Body:", body_details)


    tag = summary.find('.t-javascript', first=True).text  #Question Tag HTML class id
    print("Tags:", tag.split())
    print()

    csv_writer.writerow([headline, body, tag])  #file save

csv_file.close()

