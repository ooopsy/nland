from util import my_http, dbaccess


NEW_LAND_REGION_URL = 'https://new.land.naver.com/api/regions/list?cortarNo='
NEW_LAND_COMPLEX_URL = 'https://new.land.naver.com/api/regions/complexes?cortarNo='


START_LEVEL = 0;



def get_save_region(cortar_no):
    res = my_http.send_request(NEW_LAND_REGION_URL + cortar_no)
    c_cortar = res['regionList']

    for child in c_cortar:

        type = child['cortarType']
        no = child['cortarNo']

        if type != 'sec':
            child['rpNo'] = cortar_no
            dbaccess.save_region(child)
            get_save_region(no)
        else:
            save_complex(no)


def save_region(parent_no, region):
    print("save")


def save_complex(cortarNo):
   res = my_http.send_request(NEW_LAND_COMPLEX_URL + cortarNo)

   for complex in res['complexList']:
       dbaccess.save_complex(complex)


if __name__ == "__main__":
    get_save_region('4119000000')






