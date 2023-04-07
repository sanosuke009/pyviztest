from allure_commons.types import AttachmentType

localExecution = True # To check between local and vm/docker execution
reportPath = 'allure-results/'
implicitwait = 5000
explicitwait = 5000
browsername = 'chrome'
headless = True
browserargs = ["--start-maximized"]

user_data_dir = "./web/user_data_dir"
playwright_videos_dir = "./recorded-videos/"
playwright_traces_dir = "./test-results/"

visualtestresults = "./VisualTestResults/"
updatesnapshot = False
savefailuresnapondisk = False
allurereport = True

attachmenttype = AttachmentType.PNG