import datetime

def year():
    ____now = datetime.datetime.now()
    return str(____now.year)

def month():
    ____now = datetime.datetime.now()
    return str(____now.month).zfill(2)

def day():
    ____now = datetime.datetime.now()
    return str(____now.day).zfill(2)

def hour():
    ____now = datetime.datetime.now()
    return str(____now.hour).zfill(2)

def minute():
    ____now = datetime.datetime.now()
    return str(____now.minute).zfill(2)

def second():
    ____now = datetime.datetime.now()
    return str(____now.second).zfill(2)


def yyyymmdd():
    return year()+month()+str(day())


def yyyymmddhhmmss():
    return yyyymmdd()+hour()+minute()+second()

if __name__ == '__main__':

    print(yyyymmdd())