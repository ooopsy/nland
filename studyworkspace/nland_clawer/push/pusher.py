from util import dbaccess
from util import sender
import json

__ARTICLE_DETAIL__ = 'https://land.naver.com/article/articleDetailInfo.nhn?atclNo={0}'



def push(time):
    user_nos =dbaccess.get_time_push_users(time)
    for user_no in user_nos:
        user_no = user_no.decode('utf-8')
        user_info = dbaccess.get_user_info(user_no)
        user_info = json.loads(user_info.decode('utf-8').replace("'", '"'))
        user_articles = dbaccess.get_user_pushlist(user_no)

        message = ''
        for article_no in user_articles:
            article_no = article_no.decode('utf-8')
            article = dbaccess.get_article_detail(article_no)
            article = json.loads(article.decode('utf-8').replace("'", '"').replace("True", '"True"').replace("False", '"False"'))
            article_name = article['articleName']
            article_link = __ARTICLE_DETAIL__.format(article['articleNo'])

            message += '\r\n'
            message += '\r\n'
            message += '명:' + article_name
            message += '\r\n'
            message += '링크:<a>{0}</a>'.format(article_link)



        sender.send(user_info['email'], message.encode('utf-8'))


if __name__ == '__main__':
    push(1600)
    #dbaccess.delete("uno:li:pushlist")
