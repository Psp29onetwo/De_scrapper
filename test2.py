from datetime import datetime


def convertTimestampToDate(timeStamp):
    timeStamp = timeStamp / 1000
    dt_object = datetime.fromtimestamp(timeStamp)
    temp_string = str(convertTimestampToDate(timeStamp))[0:10]
    return temp_string

timeStamp = 1575982593000
str = convertTimestampToDate(timeStamp)