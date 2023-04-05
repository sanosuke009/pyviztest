from com.tests.pageobjects.demoblaze.launchpage import launchpage
from com.tests.baseClass.baseclass import baseclass
from com.tests.playwrighttests.demoblaze.conftest import demoblazetestdatafilepath
import pytest


@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(demoblazetestdatafilepath)
    base.page.goto(base.tm.gets("url"))
    yield base

@pytest.mark.parametrize(
    "keyword",
    ["demoblazelogin"],
)
def test_web_login(base:baseclass, keyword):
    base.setkeyword(keyword)
    launchpageobj = launchpage(base)
    assert launchpageobj.login(base.testdata.get("username"), base.testdata.get("password")) == True
    #base.visual.visualtest()