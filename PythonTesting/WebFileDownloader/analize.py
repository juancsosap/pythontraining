# -*- coding: utf-8 -*-

import os
import io
from threading import Thread
from threading import Lock
from time import time
from time import sleep

# pip install requests
import requests


class TimeDelta:

    def __init__(self, tdelta):
        tst = int(tdelta)
        tus = int((tdelta - tst) * 1000000)
        self.__microseconds = tus

        tmt = tst // 60
        ts = round((tst / 60 - tmt) * 60)
        self.__seconds = ts

        tht = tmt // 60
        tm = round((tmt / 60 - tht) * 60)
        self.__minutes = tm

        tdt = tht // 24
        th = round((tht / 24 - tdt) * 24)
        self.__hours = th

        self.__days = tdt

    @property
    def microseconds(self):
        return self.__microseconds

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__minutes

    @property
    def hours(self):
        return self.__hours

    @property
    def days(self):
        return self.__days

    def __str__(self):
        return f'{self.days}d{self.hours:02}h{self.minutes:02}:{self.seconds:02}.{self.microseconds:06}'


class URL:

    def __init__(self, url):
        self.__url = url

    @property
    def url(self):
        return self.__url

    def __eq__(self, other):
        return self.url == other.url

    def __neq__(self, other):
        return self.url != other.url

    @property
    def ext(self):
        return self.filename[self.filename.rfind('.') + 1:]

    @property
    def filename(self):
        return self.path[self.path.rfind('/') + 1:]

    @property
    def protocol(self):
        return self.url[:self.url.find(':')]

    @property
    def domain(self):
        domain = self.url[self.url.find(':') + 3:]
        return domain[:domain.find('/')]

    @property
    def path(self):
        end = self.url.find('?')
        end = end if end >= 0 else len(self.url)
        return self.url[self.url.find(':') + 3:end]

    @property
    def urldir(self):
        return self.path[len(self.domain) + 1:len(self.path) - len(self.filename)]


class fileURL(URL):

    def __init__(self, url, dir):
        URL.__init__(self, url)
        self.__dir = dir

    @property
    def dir(self):
        return self.__dir


class WebAnalizer:

    tLock = Lock()
    tCount = 0
    fCount = 0

    webs = []
    fileURLs = []

    @classmethod
    def getURLs(cls, pageStr):
        result = []

        splitText = pageStr.split(' href=')
        splitText.pop(0)
        for line in splitText:
            delimiter = line[0]
            end = line.find(delimiter, 1)
            url = line[1:end]
            result.append(URL(url))

        return result

    @classmethod
    def analizeURL(cls, url):
        try:
            cls.tCount += 1
            print(f'{cls.tCount} : {url.url}')
            filePath = os.path.join('temps', url.path.replace('/', '_'))

            if not os.path.exists(filePath):
                r = requests.get(url.url)
                with io.open(filePath, 'wb') as fileUrl:
                    fileUrl.write(r.content)

            with io.open(filePath, 'r', errors='ignore') as file:
                text = file.read()

            urls = cls.getURLs(text)
            surls = []
            fileurls = []
            for urlv in urls:
                if urlv.ext == 'pdf':
                    path = text.split('Category:</dt><dd> <a href="http://www.allitebooks.com/')[1]
                    path = os.path.join('outputs', path[:path.find('"')])
                    if not os.path.exists(path):
                        os.makedirs(path)
                    print(f'{cls.tCount} : {path}{urlv.filename}')
                    file = fileURL(urlv.url, path)
                    fileurls.append(file)
                if urlv.ext == '' or urlv.ext == 'php' or urlv.ext == 'html':
                    surls.append(urlv)

            for url in surls:
                if url not in cls.webs:
                    if cls.webs[0].domain in url.url:
                        if url.ext == '':
                            cls.tLock.acquire()
                            cls.webs.append(url)
                            cls.tLock.release()
            for fileurl in fileurls:
                if fileurl not in cls.fileURLs:
                    cls.tLock.acquire()
                    cls.fileURLs.append(fileurl)
                    cls.tLock.release()

            cls.tCount -= 1

        except Exception as e:
            raise e

    @classmethod
    def downloadFile(cls, fileurl):
        path = os.path.join(fileurl.dir, fileurl.filename)
        if not os.path.exists(path):
            cls.tCount += 1
            print(f'{cls.tCount} : {fileurl.url}')
            r = requests.get(fileurl.url)
            with io.open(path, 'wb') as fileUrl:
                fileUrl.write(r.content)
            cls.tCount -= 1
            return True
        return False

    @classmethod
    def analizeWebPage(cls, url):
        cls.webs = [URL(url)]

        li = 0
        jji = 0
        tl = []
        while len(cls.webs) > li:
            tl.append(Thread(target=cls.analizeURL, args=(cls.webs[li],)))
            tl[li].start()
            while cls.tCount > 500:
                sleep(1)
            li += 1
            if li == len(cls.webs):
                for ji in range(jji, li):
                    tl[ji].join()
                jji = li
        del tl

        i = 0
        t = []
        for fileurl in cls.fileURLs:
            t.append(Thread(target=cls.downloadFile, args=(fileurl,)))
            t[i].start()
            while cls.tCount > 20:
                sleep(1)
            i += 1
        for j in range(i):
            t[j].join()

        return (li, len(cls.fileURLs))


if __name__ == '__main__':
    url = 'http://www.allitebooks.com/page/1/'

    t0 = time()
    links, files = WebAnalizer.analizeWebPage(url)
    t1 = time()
    td = TimeDelta(t1 - t0)

    print(f'Total Files Downloaded: {files:,}')
    print(f'Total Links Analized: {links:,}')
    print(f'Time Required to complete the Task: {td}.')
