from __future__ import print_function
from util import my_http
from util import dbaccess
from util import numeric


from lxml.cssselect import CSSSelector

NEW_NAVER_LAND_URL = 'https://new.land.naver.com/api/articles/complex/{0}?tradeType=A1&page={1}'


def artical(complex_no, pageno):
    res = my_http.send_request(NEW_NAVER_LAND_URL.format(complex_no, pageno));

    for ar in res['articleList']:
        key = "cNo:" + complex_no + ":articalNo:" + ar['articleNo'] + ":price:" + numeric.amt_number(ar['dealOrWarrantPrc'])
        ar['key'] = key

        exits = dbaccess.exit_artical(ar)
        if exits > 0 :
            print('has:' + key)

        dbaccess.save_artical(ar)

    if res['isMoreData'] :
        artical(complex_no, pageno +1)


if __name__ == '__main__' :
    complexes = ('14543', '10689', '25606', '14544', '102807', '102691')

    for complex in complexes:
        artical(complex, 1)









