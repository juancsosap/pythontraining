import datetime
import pytz  # pip install pytz


class Clock:
    @staticmethod
    def currentTime(timezone):
        utcnow = datetime.datetime.now(tz=pytz.UTC)
        tznow = utcnow.astimezone(pytz.timezone(timezone))
        return tznow.strftime('%A - %B %d, %Y %H:%M:%S.%f UTC%z')


if __name__ == '__main__':
    for tz in pytz.all_timezones:
        if '/' in tz:
            continent, city = tuple(tz.split('/', 1))
        else:
            continent, city = None, tz

        if (continent == 'America') and \
           (city in ['Santiago', 'Caracas', 'Lima']):
            print(f'{Clock.currentTime(tz)} : {tz}')
