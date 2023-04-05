from typing import Any
from com.pyviztestcore.pyviztestmain import VisualTestMain

class VisualTest:

    def __init__(self, snapshot_path:str='', driverpage:Any='', updatesnapshot=False):
        self.visual = VisualTestMain(snapshot_path, driverpage, updatesnapshot)

    def setpaths(self, updatesnapshot=False) -> None:
        self.visual.setpaths(updatesnapshot)

    def visualtest_web(self, *, stepname = '', threshold: float = 0.1, 
                   fail_fast=False, updatesnapshot=False, fullpage = True, snapshot_of_locators:list=[],
                   exclude_locators:list=[]) -> bool:
        return self.visual.visualtest_web(stepname=stepname, threshold=threshold, 
                                   fail_fast=fail_fast, updatesnapshot=updatesnapshot, fullpage=fullpage,
                                     snapshot_of_locators=snapshot_of_locators, 
                                     exclude_locators=exclude_locators)
    
    def getGoldenSnapshot(self):
        return self.visual.golden_snapshot
    
    def getGoldenSnapshotName(self) -> str:
        return self.visual.golden_snapshot_name
    
    def getExpectedSnapshot(self):
        return self.visual.expected_snapshot
    
    def getExpectedSnapshotName(self) -> str:
        return self.visual.expected_snapshot_name
    
    def getDiffSnapshot(self):
        return self.visual.diff_snapshot
    
    def getDiffSnapshotName(self) -> str:
        return self.visual.diff_snapshot_name
    