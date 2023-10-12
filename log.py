import time

def timestamp(old):
    def new():
        print(time.ctime())
        old()
    return new
