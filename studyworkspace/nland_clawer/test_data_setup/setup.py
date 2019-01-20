from util import  dbaccess
import json

if __name__ == '__main__':



    default_user_info = json.loads('{"user_no": "1000000001", "user_name": "oopsy", "email": "jintian8899@gmail.com", "passwd": "shinimaa"}')
    dbaccess.save_user_info(default_user_info)

    dbaccess.add_time_push_users('1600', default_user_info['user_no'])

    complexes =  ('14543', '10689', '25606', '14544', '102807', '102691')
    for complexNo in complexes:
        dbaccess.add_user_complexes(complexNo, '1000000001')



