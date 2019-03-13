# -*- coding:utf-8 -*-
import unittest

from db import MemoryDB


class TestMemoryDB(unittest.TestCase):

    def setUp(self):
        self.db = MemoryDB()

    def tearDown(self):
        pass

    def test_create(self):
        # Success Creation
        value = 'DATA'
        index = self.db.create(value)
        self.assertEqual(self.db.retrive(index), value)

        # Failed Creation
        with self.assertRaises(TypeError):
            self.db.create()

        # Data Deleting
        self.db.delete(value)

        print('TestMemoryDB test_create Loaded')

    def test_retrive(self):
        # Initial Data Loaded
        value = 'DATA'
        index = self.db.create(value)

        # Success Retriving
        self.assertEqual(self.db.retrive(index), value)
        # Last Element Recovery
        self.assertEqual(self.db.retrive(-1), value)

        # Failed Retriving
        with self.assertRaises(IndexError):
            self.db.retrive(100000)
        with self.assertRaises(TypeError):
            self.db.retrive()

        # Data Deleting
        self.db.delete(value)

        print('TestMemoryDB test_retrive Loaded')

    def test_retrive_all(self):
        # Initial Data Loaded
        testindex = []
        for i in range(10):
            testindex.append(self.db.create('DATA{}'.format(i)))
        count = len(self.db.retrive_all())

        # Success Retriving
        self.assertEqual(len(self.db.retrive_all()), count)

        # Data Deleting
        for i in range(9, -1, -1):
            value = self.db.retrive(testindex[i])
            self.db.delete(value)

        print('TestMemoryDB test_retrive_all Loaded')

    def test_update(self):
        # Initial Data Loaded
        value = 'DATA'
        index = self.db.create(value)

        # Success Updating
        newvalue = 'DATAN'
        self.db.update(index, newvalue)
        self.assertEqual(self.db.retrive(index), newvalue)
        # Failed Updating
        with self.assertRaises(ValueError):
            self.db.update('DATA', value)
        with self.assertRaises(TypeError):
            self.db.update('DATA')
        with self.assertRaises(TypeError):
            self.db.update()

        # Data Deleting
        self.db.delete(newvalue)

        print('TestMemoryDB test_update Loaded')

    def test_delete(self):
        # Initial Data Loaded
        value = 'DATA'
        self.db.create(value)

        # Success Deleting
        count = len(self.db.retrive_all())
        self.db.delete(value)
        self.assertEqual(len(self.db.retrive_all()), count - 1)

        # Failed Deleting
        with self.assertRaises(ValueError):
            self.db.delete('DATAX')
        with self.assertRaises(TypeError):
            self.db.update()

        print('TestMemoryDB test_delete Loaded')
