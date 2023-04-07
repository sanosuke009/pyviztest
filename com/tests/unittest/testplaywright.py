import os
from pathlib import Path
import allure
from playwright.sync_api import Page
import pytest
from com.pyviztestcore.viztest import VisualTest
from com.tests.unittest.pageobject import *
from com.tests.unittest.testdata import *
from com.tests.unittest.config import *
import shutil

@pytest.fixture(scope="function", autouse=True)
def before_each(page:Page):
    page.goto(url=url)
    yield

def test_goldensnapshot(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    if page_title in page.url:
        assert True
    assert vm.visualtest_web(stepname="launchpage")
    resultpath = (
        Path(visualtestresults)
        / "Golden_Snapshots"
        / "testplaywright"
        / "test_goldensnapshot"
    )
    shutil.rmtree(os.path.abspath(resultpath))

def test_updatesnapshot(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    if page_title in page.url:
        assert True
    assert vm.visualtest_web(stepname="launchpage")

def test_matchingsnapshot(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    if page_title in page.url:
        assert True
    assert vm.visualtest_web(stepname="launchpage")

def test_nonmatchingsnapshot(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    assert page_title in page.url
    loginlink = page.locator("xpath="+xpath_link_login)
    loginlink.click()
    loginheader = page.locator("xpath="+xpath_header_login)
    loginheader.wait_for(state='visible')
    usernamefield = page.locator("id="+id_input_username)
    passwordfield = page.locator("id="+id_input_password)
    loginbutton = page.locator("xpath="+xpath_button_login)
    #gallery = page.locator("xpath="+xpath_div_movinggallery)
    usernamefield.fill(username)
    passwordfield.fill(password)
    loginbutton.click()
    page.wait_for_load_state(state='networkidle')
    logoutlink = page.locator("xpath="+xpath_link_logout)
    logoutlink.wait_for(state='visible')
    assert vm.visualtest_web(stepname="launchpage") == False

#============Element specific tests==============================
def test_goldensnapshot_element(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    assert page_title in page.url
    loginbutton = page.locator("xpath="+xpath_link_login)
    cartbutton = page.locator("xpath="+xpath_link_cart)
    signupbutton = page.locator("xpath="+xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton])
    resultpath = (
        Path(visualtestresults)
        / "Golden_Snapshots"
        / "testplaywright"
        / "test_goldensnapshot_element"
    )
    shutil.rmtree(os.path.abspath(resultpath))

def test_updatesnapshot_element(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    assert page_title in page.url
    loginbutton = page.locator("xpath="+xpath_link_login)
    cartbutton = page.locator("xpath="+xpath_link_cart)
    signupbutton = page.locator("xpath="+xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton])
    

def test_matchingsnapshot_element(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    assert page_title in page.url
    loginbutton = page.locator("xpath="+xpath_link_login)
    cartbutton = page.locator("xpath="+xpath_link_cart)
    signupbutton = page.locator("xpath="+xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton])
    

def test_nonmatchingsnapshot_element(page:Page) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=page, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    page.wait_for_load_state(state='networkidle')
    page.wait_for_selector("xpath="+xpath_header_productstore)
    assert page_title in page.url
    loginbutton = page.locator("xpath="+xpath_link_login)
    cartbutton = page.locator("xpath="+xpath_link_cart)
    signupbutton = page.locator("xpath="+xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton]) == False
                                                                          
    

#============Multiple snapshot in a single test==============================
def test_goldensnapshot_multi(page:Page) -> None:
    pass

def test_updatesnapshot_multi(page:Page) -> None:
    pass

def test_matchingsnapshot_multi(page:Page) -> None:
    pass

def test_nonmatchingsnapshot_multi(page:Page) -> None:
    pass