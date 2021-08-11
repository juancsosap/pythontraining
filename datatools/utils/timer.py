import datetime as dt

class TimeUtils:
    # convert from string to datetime using the template
    @staticmethod
    def todatetime(value, template='%Y-%m-%d %H:%M:%S'):
        return dt.datetime.strptime(value, template)
    
    # fix the datetime from utc, based on timezone change days
    # and the local gmt. The wcdr is for the winter change date and the
    # scdr is the summer change date. Both are presented in the format
    # "<dayofweek>-<month>"
    @staticmethod
    def fixdatetime(utcvalue, wcdr="6-04", scdr="6-09", gmt=-3, template=None):
        if type(utcvalue) is str:
            if template is None:
                template = '%Y/%m/%d %H:%M:%S' if '/' in utcvalue else '%Y-%m-%d %H:%M:%S'
            utcvalue = TimeUtils.todatetime(utcvalue, template)
        wcd = TimeUtils.finddatetime(utcvalue.year, int(wcdr[-2:]), int(wcdr[0]))
        scd = TimeUtils.finddatetime(utcvalue.year, int(scdr[-2:]), int(scdr[0]))
        hours = (gmt - 1) if (utcvalue > wcd) and (utcvalue < scd) else gmt
        delta = dt.timedelta(hours=hours)
        return utcvalue + delta

    # find a date in the week from year, month, day of the
    # week and count, where monday is 1 and sunday is 7  
    @staticmethod
    def finddatetime(year, month, dayofweek, count=1):
        fdt = dt.datetime(year, month, 1)
        days = (dayofweek - fdt.weekday() + 6) % 7 + (count-1)*7
        return fdt + dt.timedelta(days=days)
