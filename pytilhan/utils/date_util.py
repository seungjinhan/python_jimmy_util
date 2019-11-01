import datetime
____now = datetime.datetime.now()
def year():
    return str(____now.year)

def month():
    return str(____now.month).zfill(2)

def day():
    return str(____now.day).zfill(2)

def hour():
    return str(____now.hour).zfill(2)

def minute():
    return str(____now.minute).zfill(2)

def second():
    return str(____now.second).zfill(2)


def yyyymmdd():
    return year()+month()+str(day())


def yyyymmddhhmmss():
    return yyyymmdd()+hour()+minute()+second()

if __name__ == '__main__':

    print(yyyymmdd())