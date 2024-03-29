import csv
from requests_html import HTML, HTMLSession
session = HTMLSession()

# File Save as CSV Format
csv_file = open('44st_bcsTest.csv', 'w') #save file name
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Question No','Question', 'Options']) #column name

res = session.get('https://uttoron.academy/question/44th-bcs/') #link

questions = res.html.find('.question-item') #HTML parent id (by '.' catch the html class)

for summary in questions:
    question = summary.find('.question > p', first=True).text  #Question Headline HTML class id
    # print("Question:", question)

    question_id = summary.find('.question > h2', first=True).text  # Question Headline HTML class id
    # print("Question No:", question_id)

    options = summary.find('.options', first=True).text  #Question Body HTML class id
    # print("Options:\n", options)

    csv_writer.writerow([question_id +'\n' + question +'\n' + options])
    print('question=====: ', question)

csv_file.close()



# Normal Bangla Way
# questions = res.html.find('.question-item') #HTML parent id (by '.' catch the html class)
#
# for question in questions:
#     headline = question.find('.question > p', first=True).text  #Question Headline HTML class id
#     print("Headline:", headline)
#
# for options in questions:
#     opt = options.find('.options', first=True).text  #Question Headline HTML class id
#     print("options:", opt)
#

