from datetime import datetime, timedelta

class Mode:

    def GetDefaultTimestamp():
        date = datetime.now()
        timestamp = int(date.timestamp())
        print('Timestamp:', timestamp)

    def GetTimestampToDate():
        date = input('Введите дату через точку >> ')
        date = date.split('.')
        date = [int(i) for i in date]
        day = date[0]
        month = date[1]
        year = date[2]

        suka = datetime(year=year, month=month, day=day)
        timestamp = int(suka.timestamp())
        print('Дата:', suka)
        print('Timestamp:', timestamp)

    def AddMinuteToTimestamp():
        minute = int(input('Введите минуты >> '))
        time_delta = timedelta(minutes=minute)
        current_time = datetime.now()
        future_time = time_delta + current_time
        timestamp = int(future_time.timestamp())
        print('Дата:', future_time)
        print('Timestamp:', timestamp)

    def AddHourToTimestamp():
        hour = int(input('Введите часы >> '))
        time_delta = timedelta(hours=hour)
        current_time = datetime.now()
        future_time = time_delta + current_time
        timestamp = int(future_time.timestamp())
        print('Дата:', future_time)
        print('Timestamp:', timestamp)

    def AddWeekToTimestamp():
        week = int(input('Введите недели >> '))
        time_delta = timedelta(weeks=week)
        current_time = datetime.now()
        future_time = time_delta + current_time
        timestamp = int(future_time.timestamp())
        print('Дата:', future_time)
        print('Timestamp:', timestamp)
