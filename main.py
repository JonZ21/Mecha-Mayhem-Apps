from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TOTAL_TEAMS = 121
TOTAL_MATCHES = 100

options = webdriver.ChromeOptions() 
options.headless = False
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging']) # supress console messages
url = 'https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-22-0596.html#results-' 

driver = webdriver.Chrome(service=ChromeService( 
    ChromeDriverManager().install()), options=options) 
 

driver.maximize_window()
driver.get(url) 

driver.implicitly_wait(10)

#team list
for team in range(1,TOTAL_TEAMS):
    try:
        addressName = "//*/div[3]/div/div/div[2]/div/div/div/section[12]/div/table/tbody/tr[" + str(team) + "]/td[1]/a"
        number = driver.find_element(By.XPATH, addressName).text
        # collection.insert_one({"team": number, "photo": image_bytes.getvalue()})
    except NoSuchElementException:
        print("exception")
        break    

# skills
for count in range(1,TOTAL_TEAMS):
    try:
        addressName = "//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[1]/div[1]/div/table/tbody/tr[" + str(count) + "]/td[2]"
        addressScore = "//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[1]/div[1]/div/table/tbody/tr[" + str(count) + "]/td[7]"
        print(f"{driver.find_element(By.XPATH, addressName).text} scored {driver.find_element(By.XPATH,addressScore).text}")
    except NoSuchElementException:
        print("exception")
        break


#navigate to division 1
url = 'https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-22-7814.html#teams'
division1 = driver.find_element(By.LINK_TEXT, "Division 1")
division1.click()
time.sleep(1)

for match in range(1,TOTAL_MATCHES):
    try:
        aNumber = driver.find_element(By.XPATH, "//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[1]").text.split()
        ar1 = driver.find_element(By.XPATH,"//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[2]").text
        ar2 = driver.find_element(By.XPATH,"//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[3]").text
        arScore = driver.find_element(By.XPATH,"//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[5]").text
        ab1 = driver.find_element(By.XPATH,"//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[6]").text
        ab2 = driver.find_element(By.XPATH,"//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[7]").text
        abScore = driver.find_element(By.XPATH,"//*/div[3]/div/div/div[2]/div/div/div/section[13]/div/div/div/div[2]/div/div/div/section[2]/div[1]/div[1]/div[1]/table/tbody/tr[" + str(match) + "]/td[9]").text
        print(aNumber[0],aNumber[1], ar1, ar2, arScore, ab1, ab2, abScore)
        #This breaks this code so that if it reads finals 1 it quits
        #THIS WONT WORK WITH THE SIG EVENT BECUASE THERES AT LEAST 3 FINALS 
        if aNumber[0] == "Final":
            break
        post = {"match": aNumber[0] + aNumber[1], "r1": ar1, "r2": ar2, "ars": arScore, "b1": ab1, "b2": ab2, "abs": abScore}
        # collection.insert_one(post)
    except NoSuchElementException:
        print("exception")
        break

# print(matchNumber, r1, r2, rScore, b1, b2, bScore)

print("finished")
driver.quit()
