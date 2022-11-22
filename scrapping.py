import csv
from requests_html import HTMLSession


# File Save as CSV Format
csv_file = open('js1000.csv', 'w')  # save file name
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Questions', 'Body', 'Tags'])  # column name


session = HTMLSession()
NUMBER_OF_PAGE = 1
QUESTIONS_BANK = []


def get_question_detail(url=None):
    if url is not None:
        que_detail = session.get(url)
        title = que_detail.html.find('#question-header > h1 > a', first=True).text
        body = que_detail.html.find('#question > div > div.postcell.post-layout--right > div.s-prose.js-post-body',
                                    first=True).text

        tag = que_detail.html.find('.question > div.post-layout > div.postcell.post-layout--right > div.mt24.mb12 > div > div > a')

        tags = [x.text for x in tag]
        all_tags = ','.join(tags)

        # tag = que_detail.html.find('.js-gps-track')
        # tag = que_detail.html.find('.ps-relative', first=True).text
        # question > div.post-layout > div.postcell.post-layout--right > div.mt24.mb12 > div > div

        QUESTIONS_BANK.append({"title": title, "body":body, "all_tags":all_tags})

        print(QUESTIONS_BANK)
        csv_writer.writerow([title, body, all_tags])

        # print("Title: ", title)
        # print("Body: ", body,)
        # # print( "Tag: ",tag)
        # print("Tags:", all_tags)
        # print()

def questions_list(page=1):
    url = session.get(
        'https://stackoverflow.com/questions/tagged/javascript?tab=votes&page=' + str(page) + '&pagesize=50')
    questions = url.html.find('.summary')
    for summary in questions:
        headline = list(summary.find('.question-hyperlink', first=True).absolute_links)[0]
        get_question_detail(headline)


def execute_program():
    for x in range(NUMBER_OF_PAGE):
        page = 1
        questions_list(page=page)
        page += 1
        # print(NUMBER_OF_PAGE)
execute_program()



# def write_csv():
#     csv_writer.writerow(QUESTIONS_BANK)
