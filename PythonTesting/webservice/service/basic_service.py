# -*- coding:utf-8 -*-

from db import MemoryDB
from flask import render_template


class BasicService:

    def __init__(self):
        self.db = MemoryDB()

    def getinfos(self):
        return render_template('infos.xml', infos=self.db.retrive_all())

    def postinfo(self):
        return "Under Construction"

    def getinfo(self, id):
        return render_template('info.xml', info=self.db.retrive(id))

    def putinfo(self, id):
        return "Under Construction"

    def deleteinfo(self, id):
        return "Under Construction"
