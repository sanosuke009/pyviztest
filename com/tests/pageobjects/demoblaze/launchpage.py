"This module contains the page object class of the launch page"
from com.tests.baseClass.baseclass import baseclass


class launchpage:

    def __init__(self, base:baseclass):
        self.base = base
        self.page = base.page
        self.rm = base.rm
        self.vm = base.visual

    # Page object locators
    page_title = 'https://www.demoblaze.com/' 
    xpath_header_productstore = "//a[contains(text(),'PRODUCT STORE')]"
    xpath_link_login = "//a[contains(text(),'Log in')]"
    xpath_link_logout = "//a[contains(text(),'Log out')]"
    xpath_link_signup = "//a[contains(text(),'Sign up')]"
    xpath_link_cart = "//a[contains(text(),'Cart')]"

    xpath_header_login = "//h5[contains(text(),'Log in')]"
    id_input_username = "loginusername"
    id_input_password = "loginpassword"
    xpath_button_close = "//button[contains(text(),'Close')]"
    xpath_button_login = "//button[contains(text(),'Log in')]"

    xpath_div_movinggallery = "//div[@class='carousel-inner']"

    # Page object methods/functions
    def login(self, username, password):
        try:
            result = True
            self.page.wait_for_load_state(state='networkidle')
            self.page.wait_for_selector("xpath="+self.xpath_header_productstore)
            if self.page_title in self.page.url:
                self.rm.addscreenshot("Launch page is launched.")
                viz = self.vm.visualtest_web(stepname=self.base.getkeyword()+"_afterlogin")
                if viz == False:
                    self.rm.addscreenshot(self.vm.getGoldenSnapshotName(), self.vm.getGoldenSnapshot())
                    self.rm.addscreenshot(self.vm.getExpectedSnapshotName(), self.vm.getExpectedSnapshot())
                    self.rm.addscreenshot(self.vm.getDiffSnapshotName(), self.vm.getDiffSnapshot())
                    result = False
                loginlink = self.page.locator("xpath="+self.xpath_link_login)
                viz =self.vm.visualtest_web(snapshot_of_locators=[loginlink])
                if viz == False:
                    self.rm.addscreenshot(self.vm.getGoldenSnapshotName(), self.vm.getGoldenSnapshot())
                    self.rm.addscreenshot(self.vm.getExpectedSnapshotName(), self.vm.getExpectedSnapshot())
                    self.rm.addscreenshot(self.vm.getDiffSnapshotName(), self.vm.getDiffSnapshot())
                    result = False
                loginlink.click()
                loginheader = self.page.locator("xpath="+self.xpath_header_login)
                loginheader.wait_for(state='visible')
                usernamefield = self.page.locator("id="+self.id_input_username)
                passwordfield = self.page.locator("id="+self.id_input_password)
                loginbutton = self.page.locator("xpath="+self.xpath_button_login)
                gallery = self.page.locator("xpath="+self.xpath_div_movinggallery)
                usernamefield.fill(username)
                passwordfield.fill(password)
                self.rm.addscreenshot("Credential fields are filled in.")
                loginbutton.click()
                self.rm.addscreenshot("Login button is clicked.")
                self.page.wait_for_load_state(state='networkidle')
                logoutlink = self.page.locator("xpath="+self.xpath_link_logout)
                logoutlink.wait_for(state='visible')
                if self.page.is_visible("xpath="+self.xpath_link_logout):
                    self.rm.addscreenshot("Login successful!")
                    viz =self.vm.visualtest_web(snapshot_of_locators=[logoutlink])
                    if viz == False:
                        self.rm.addscreenshot(self.vm.getGoldenSnapshotName(), self.vm.getGoldenSnapshot())
                        self.rm.addscreenshot(self.vm.getExpectedSnapshotName(), self.vm.getExpectedSnapshot())
                        self.rm.addscreenshot(self.vm.getDiffSnapshotName(), self.vm.getDiffSnapshot())
                        result = False
                    viz = self.vm.visualtest_web(stepname=self.base.getkeyword()+"_beforelogin", exclude_locators=[gallery])
                    if viz == False:
                        self.rm.addscreenshot(self.vm.getGoldenSnapshotName(), self.vm.getGoldenSnapshot())
                        self.rm.addscreenshot(self.vm.getExpectedSnapshotName(), self.vm.getExpectedSnapshot())
                        self.rm.addscreenshot(self.vm.getDiffSnapshotName(), self.vm.getDiffSnapshot())
                        result = False
                    return result
                else:
                    self.rm.addscreenshot("Error occurred during Login.")
                    self.vm.visualtest_web(stepname=self.base.getkeyword()+"_beforelogin", exclude_locators=[gallery])
                    return False
            else:
                self.rm.addscreenshot("Launch page is NOT launched.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during launch page launch and login.")
            print(e)
            return False
        else:
            return True

