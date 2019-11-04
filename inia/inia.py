from selenium  import webdriver
from datetime import datetime
import sys

wod = {
    0:5,    #MONDAY on Column 6
    1:6,
    2:7,
    3:8,
    4:9,
    5:10,
    6:0
}

td = wod[datetime.today().weekday()]
print(td)

print("Initiating Driver")
driver = webdriver.Chrome("/usr/bin/chromedriver")
#driver = webdriver.Chrome("/data/data/com.termux/files/home/chromedriver")

print("Launching Inia PRO")
driver.get("https://iniapro.objectfrontier.com/")

print("Login with username Password")
driver.find_element_by_id("username").send_keys("sankaranarayanan.s")
driver.find_element_by_id("password").send_keys(os.environ["PASSWORD"])
driver.find_element_by_id("login-submit").click()
print("Exiting Test Case")
sys.exit(1)
driver.find_element_by_link_text("Time Entries").click()
driver.find_element_by_xpath("//tr[1]//td[5]//a[1]//img[1]").click()
driver.find_element_by_link_text("Add Row").click()
driver.find_element_by_xpath("//table[@id='issueTable']//tbody/tr[last()-1]/td[2]/select[@id='time_entry__issue_id']/option[text()='Support #52074: Self Learning DevOps']").click()
driver.find_element_by_xpath("//table[@id='issueTable']//tbody/tr[last()-1]/td[3]/select[@id='time_entry__activity_id']/option[text()='Support']").click()
driver.find_element_by_xpath("//table[@id='issueTable']//tbody/tr[last()-1]/td["+ str(td) +"]/div[1]/input[1]").send_keys("8")
driver.find_element_by_id("wktime_save").click()
driver.find_element_by_link_text("Sign out").click()

