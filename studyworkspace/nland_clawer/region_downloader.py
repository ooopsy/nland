import requests
import json
import pymongo



NEW_LAND_REGION_URL = 'https://new.land.naver.com/api/regions/list?cortarNo='
NEW_LAND_COMPLEX_URL = 'https://new.land.naver.com/api/regions/complexes?cortarNo='

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
START_LEVEL = 0;



def get_region_list(cortarNo):
    res = send_request(NEW_LAND_REGION_URL + cortarNo)
    cortar_children = res['regionList']

    for child in cortar_children:
        cortarType = child['cortarType']
        cortarNo = child['cortarNo']

        if cortarType == 'sec':
            get_complex_list(cortarNo)
        else:
            get_region_list(cortarNo)


def get_complex_list(cortarNo):
   res =  send_request(NEW_LAND_COMPLEX_URL + cortarNo)
   print(res['complexList'])



def send_request(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    response = session.get(url)
    return json.loads(response.text)


if __name__ == "__main__":
    get_region_list('0000000000');






