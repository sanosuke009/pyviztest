import os
from pathlib import Path
import allure
from playwright.sync_api import Page
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.pyviztestcore.viztest import VisualTest
from com.tests.unittest.pageobject import *
from com.tests.unittest.testdata import *
from com.tests.unittest.config import *
import shutil

@pytest.fixture (scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(int(implicitwait)/1000)
    driver.get(url=url)
    yield driver
    driver.quit()

def test_selenium_goldensnapshot(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    assert vm.visualtest_web(stepname="launchpage")
    resultpath = (
        Path(visualtestresults)
        / "Golden_Snapshots"
        / "test_selenium"
        / "test_selenium_goldensnapshot"
    )
    shutil.rmtree(os.path.abspath(resultpath))

def test_selenium_updatesnapshot(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    assert vm.visualtest_web(stepname="launchpage")

def test_selenium_matchingsnapshot(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    assert vm.visualtest_web(stepname="launchpage")

def test_selenium_nonmatchingsnapshot(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    loginlink = browser.find_element(By.XPATH, xpath_link_login)
    loginlink.click()
    loginheader = browser.find_element(By.XPATH, xpath_header_login)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_login)))
    usernamefield = browser.find_element(By.ID, id_input_username)
    passwordfield = browser.find_element(By.ID, id_input_password)
    loginbutton = browser.find_element(By.XPATH, xpath_button_login)
    #gallery = page.locator("xpath="+xpath_div_movinggallery)
    usernamefield.send_keys(username)
    passwordfield.send_keys(password)
    loginbutton.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_link_logout)))
    assert vm.visualtest_web(stepname="launchpage") == False

#============Element specific tests==============================
def test_selenium_goldensnapshot_element(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    loginbutton = browser.find_element(By.XPATH, xpath_link_login)
    cartbutton = browser.find_element(By.XPATH, xpath_link_cart)
    signupbutton = browser.find_element(By.XPATH, xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton])
    resultpath = (
        Path(visualtestresults)
        / "Golden_Snapshots"
        / "test_selenium"
        / "test_selenium_goldensnapshot_element"
    )
    shutil.rmtree(os.path.abspath(resultpath))

def test_selenium_updatesnapshot_element(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths(updatesnapshot=True)
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    loginbutton = browser.find_element(By.XPATH, xpath_link_login)
    cartbutton = browser.find_element(By.XPATH, xpath_link_cart)
    signupbutton = browser.find_element(By.XPATH, xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton])
    

def test_selenium_matchingsnapshot_element(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    loginbutton = browser.find_element(By.XPATH, xpath_link_login)
    cartbutton = browser.find_element(By.XPATH, xpath_link_cart)
    signupbutton = browser.find_element(By.XPATH, xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton])
    

def test_selenium_nonmatchingsnapshot_element(browser) -> None:
    vm = VisualTest(snapshot_path=visualtestresults, driverpage=browser, updatesnapshot=updatesnapshot, 
                    savefailuresnapondisk=savefailuresnapondisk, allurereport=allurereport)
    vm.setpaths()
    headerelement = browser.find_element(By.XPATH, xpath_header_productstore)
    wait = WebDriverWait(browser, int(explicitwait)/1000)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_header_productstore)))
    assert page_title in browser.current_url
    assert headerelement.is_displayed()
    loginbutton = browser.find_element(By.XPATH, xpath_link_login)
    cartbutton = browser.find_element(By.XPATH, xpath_link_cart)
    signupbutton = browser.find_element(By.XPATH, xpath_link_signup)
    assert vm.visualtest_web(stepname="launchpage", snapshot_of_locators=[loginbutton
                                                                          , cartbutton, signupbutton]) == False
                                                                          
    

#============Multiple snapshot in a single test==============================
def test_selenium_goldensnapshot_multi(browser) -> None:
    pass

def test_selenium_updatesnapshot_multi(browser) -> None:
    pass

def test_selenium_matchingsnapshot_multi(browser) -> None:
    pass

def test_selenium_nonmatchingsnapshot_multi(browser) -> None:
    pass