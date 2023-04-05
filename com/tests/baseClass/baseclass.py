
from com.pyviztestcore.viztest import VisualTest
from playwright.sync_api import Page
from com.tests.playwrighttests.managers.resultmanager import resultmanager
from com.tests.managers.testdatamanager import testdatamanager
from com.tests.config.propConfig import visualtestresults, updatesnapshot


class baseclass:

    def __init__(self, page:Page) -> None:
        self.rm = resultmanager(page)
        self.page = page
        self.visual = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot)

    def settestdatamanager(self, testdatafilepath):
        self.tm = testdatamanager(testdatafilepath)

    def setkeyword(self, keyword):
        self.keyword = keyword
        self.visual.setpaths()
        self.settestdata()

    def getkeyword(self) -> str:
        return self.keyword
    
    def settestdata(self):
        self.testdata = self.tm.gets(self.keyword)
    
    def gettestdata(self):
        return self.testdata