"This class controls the visual testing"

from typing import Any
from allure_commons.types import AttachmentType
import allure
from playwright.sync_api import Page, Locator
from com.tests.config.propConfig import visualtestresults


class visualtestmanager:

    def __init__(self, page : Page, assert_snapshot):
        self.page = page
        self.assert_snapshot = assert_snapshot

    def visualtest(self, name:str, locator:Any='', fullpage = True, mask=[], threshold=0.1, fail_fast  = False):
        if type(locator) == Locator:
            self.assert_snapshot(locator.screenshot(), snapshot_path=visualtestresults, threshold =threshold, fail_fast=fail_fast, name=name)
        else:
            self.assert_snapshot(self.page.screenshot(full_page=fullpage, mask=mask), snapshot_path=visualtestresults, threshold =threshold, fail_fast=fail_fast, name=name)


    def deprecated_visualtest(self, name:str, fullpage = True, mask=[], threshold=0.1, fail_fast  = False):
        #allure.attach(self.page.screenshot(), name=message, attachment_type=AttachmentType.PNG)
        self.assert_snapshot(self.page.screenshot(full_page=fullpage, mask=mask), snapshot_path=visualtestresults, threshold =threshold, fail_fast=fail_fast, name=name)

    def visualtestassert(self, fullpage = True, mask=[], threshold=0.1, fail_fast  = False):
        #allure.attach(self.page.screenshot(), name=message, attachment_type=AttachmentType.PNG)
        self.assert_snapshot(self.page.screenshot(full_page=fullpage, mask=mask), threshold =threshold, fail_fast=fail_fast)