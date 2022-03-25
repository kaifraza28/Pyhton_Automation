import sqlite3
import unittest

class Patients(unittest.TestCase):
    def setUp(self):
        #making connection
        self.connection = sqlite3.connect("Hospital.db")
        self.Patient_Code ="1"
        self.Patient_name = "Kaif"
    def tearDown(self):
        self.Patient_Code = "0"
        self.Patient_name =""
        self.connection.close()

    def test_pat1(self):
        result = self.connection.execute("SELECT Patient_name FROM Hospital where Patient_Code ="+self.Patient_Code)
        for i in result:
            fetchName = i[0]
            self.assertEqual(fetchName,self.Patient_name)