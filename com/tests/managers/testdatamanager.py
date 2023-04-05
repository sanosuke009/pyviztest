import json

class testdatamanager:

    def __init__(self, testdatafile):
        self.jsonfile = open(testdatafile)
        self.testdata = json.load(self.jsonfile)

    def gets(self, testdatakey):
        return self.testdata.get(testdatakey)

    def get(self, testcaseid, testdatakey):
        return self.testdata.get(testcaseid).get(testdatakey)
