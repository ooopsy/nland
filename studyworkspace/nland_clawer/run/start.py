import schedule
import  downloader.artical
import  push.pusher

if __name__ == '__main__':
    schedule.every(8).hours.do(downloader.artical.my_artical)
    schedule.every(1).hours.do(push.pusher.push)

    while True:
        schedule.run_pending()