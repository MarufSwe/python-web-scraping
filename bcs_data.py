import csv
from requests_html import HTML, HTMLSession
session = HTMLSession()

# File Save as CSV Format
csv_file = open('xxx.csv', 'w') #save file name
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Question No','Question', 'Options', 'Explanation']) #column name

session = HTMLSession()
res = session.get('https://uttoron.academy/question/44th-bcs/') #link

questions = res.html.find('.question-item') #HTML parent id (by '.' catch the html class)

for summary in questions:
    question = summary.find('.question > p', first=True).text  #Question Headline HTML class id
    # print("Question:", question)

    question_id = summary.find('.question > h2', first=True).text  # Question Headline HTML class id
    # print("Question No:", question_id)

    options = summary.find('.options', first=True).text  #Question Body HTML class id
    # print("Options:\n", options)

    # right_options = summary.find('.options > ul > li .is_right', first=True).text  #Question Body HTML class id
    # right_options = summary.find('.options > li[class="is_right"]', first=True).text

    explanation = summary.find('.question-solve', first=True).text  # Question Body HTML class id

    # csv_writer.writerow([question_id +'\n' + question +'\n' + options +'\n'+ explanation +'\n'+ right_options])
    # csv_writer.writerow([question_id +'\n' + question +'\n' + options +'\n'+ explanation])
    csv_writer.writerow([question_id + question + options + explanation])

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

