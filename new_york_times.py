import csv
from requests_html import HTML, HTMLSession
session = HTMLSession()


# File Save as CSV Format
# csv_file = open('prothom_alo.csv', 'w') #save file name
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Question No','Question', 'Options']) #column name

session = HTMLSession()
res = session.get('https://www.nytimes.com/section/sports') #link

questions = res.html.find('.css-xei2dc') #HTML parent id (by '.' catch the html class)

for summary in questions:
    question = summary.find('.css-10wtrbd > h2', first=True)  #Question Headline HTML class id
    print("Question:", question)
#
#     question_id = summary.find('.question > h2', first=True).text  # Question Headline HTML class id
#     # print("Question No:", question_id)
#
#     options = summary.find('.options', first=True).text  #Question Body HTML class id
#     # print("Options:\n", options)
#
#     csv_writer.writerow([question_id +'\n' + question +'\n' + options])
#
# csv_file.close()


