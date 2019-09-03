# -*- coding: utf-8 -*-

import re
import os
from threading import Thread
from threading import Lock
from time import time
from time import sleep

class Word:
    def __init__(self, word, quantity):
        self.__value = word
        self.__quantity = quantity

    def getValue(self):
        return self.__value

    def getQuantity(self):
        return self.__quantity

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


class FileAnalizer:

    tLock = Lock()
    tCount = 0
    fCount = 0

    @classmethod
    def analizeFile(cls, filePath):
        try:
            words = []
            count = 0
            with open(filePath, 'r') as file:
                text = file.read()
                text = text.replace('\n', ' ')
                wordsText = text.split(' ')
                for word in wordsText:
                    word = word.lower()
                    removedChars = '%&~<>@\\°*#`\'^,;.:-—–_¿?!¡|()[]{}"“”«»$+•='
                    for char in removedChars:
                        word = word.replace(char, '')
                    if len(word) > 3 and not re.match('.*[0-9]+.*', word) and word.isprintable():
                        count += 1
                        words.append(Word(word, 1))
            return words
        except IOError as e:
            print("{filePath} not found")
            raise e

    @classmethod
    def agregateWords(cls, wordsList):
        wordsList.sort(key=lambda w: w.getValue())
        groupWord, tmpWord, q = [], '', 0
        for word in wordsList:
            if tmpWord != word.getValue():
                groupWord.append(Word(tmpWord, q))
                q = 0
            tmpWord = word.getValue()
            q += word.getQuantity()
        return groupWord

    @classmethod
    def filterResults(cls, resultPath, groupWord, fileName):
        try:
            cls.tLock.acquire()
            with open(resultPath, 'a') as outputFile:
                for word in groupWord:
                    if word.getQuantity() > 10:
                        outputFile.write(f'{fileName} : {word.getValue()} : {word.getQuantity()}\n')
            cls.tLock.release()
        except IOError as e:
            print("{filePath} not found")
            raise e

    @classmethod
    def fileReview(cls, filePath):
        cls.tCount += 1
        fileName = os.path.basename(filePath)
        print(f'{fileName} : Process {cls.tCount:,} Started')
        words = cls.analizeFile(filePath)
        groupWord = cls.agregateWords(words)
        outputPath = os.path.join(os.path.dirname(filePath), 'result.log')
        cls.filterResults(outputPath, groupWord, fileName)
        # filterResults(f'{filePath}.log', groupWord)
        print(f'{fileName} : {len(words):,} Words')
        cls.tCount -= 1
        print(f'{fileName} : Process {cls.tCount:,} Remain')
        cls.fCount += 1

    @classmethod
    def loadResults(cls, dirPath):
        try:
            resultPath = os.path.join(dirPath, 'result.log')
            words = []
            count = 0
            with open(resultPath, 'r') as resultFile:
                for line in resultFile:
                    file, word, quantity = line.split(' : ')
                    words.append(Word(word, int(quantity)))
                    count += 1
            groupWord = cls.agregateWords(words)
            groupWord.sort(key=lambda w: w.getQuantity())
            resultPath = os.path.join(dirPath, 'result-final.log')
            with open(resultPath, 'a') as outputFile:
                for word in groupWord:
                    if word.getQuantity() > 10:
                        outputFile.write(f'{word.getValue()} : {word.getQuantity():,}\n')
            return groupWord
        except IOError as e:
            print("{resultPath} not found")
            raise e

    @classmethod
    def analizeFolder(cls, filesDIR):
        t = []
        i = 0
        for file in os.listdir(filesDIR):
            fileDIR = os.path.join(filesDIR, file)
            if os.path.isfile(fileDIR):
                t.append(Thread(target=cls.fileReview, args=(fileDIR,)))
                t[i].start()
                if cls.tCount > 500:
                    sleep(1)
                i += 1
        for j in range(i):
            t[j].join()
        words = cls.loadResults(filesDIR)
        return words        


if __name__ == '__main__':
    DIR = os.getcwd()
    filesDIR = os.path.join(DIR, 'RFCs')

    t0 = time()
    words = FileAnalizer.analizeFolder(filesDIR)
    t1 = time()
    td = TimeDelta(t1 - t0)
    
    print(f'Total Words Analized: {len(words):,}')
    print(f'Total Files Analized: {FileAnalizer.fCount:,}')
    print(f'Time Required to complete the Task: {td}.')
