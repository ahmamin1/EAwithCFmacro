from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import csv
import json 

with open('config.json', 'r') as f:
    config = json.load(f)

email = config['email']
password = config['password']

def macro(sessionID):
    driver = webdriver.Chrome()
    # navigate to the easy-attend.com login page
    driver.get("https://easy-attend.com/ams/login/login.php?action=org")
    # wait for the page to load
    time.sleep(3)
    # find the username and password fields, and enter your credentials
    username_field = driver.find_element(By.NAME, "useremailTxtBox")
    username_field.send_keys(email)
    password_field = driver.find_element(By.NAME, "userPwTxtBox")
    password_field.send_keys(password)
    # submit the login form
    password_field.send_keys(Keys.RETURN)
    # wait for the page to load
    time.sleep(10)
    # navigate to the attendance page for the session you want to mark
    driver.get(
        f"https://easy-attend.com/ams/reports/session.php?sid={sessionID}")
    # wait for the page to load
    time.sleep(3)
    IDs = []
    with open('report.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        column_name = 'easyattendID'
        column_index = header.index(column_name)
        # Loop through each row in the CSV file
        for row in csv_reader:
            # Append the data in the column of interest to the list
            IDs.append(row[1])
    unsuccess = []
    i = 0
    for trainee_id in IDs:
        i += 1
        if (trainee_id != "0"):
            # find the text field to enter the trainee ID
            id_field = driver.find_element(By.NAME, "attCodeTxt")
            # enter the trainee ID
            id_field.send_keys(trainee_id)
            # submit the form to mark the attendance
            id_field.send_keys(Keys.RETURN)
            # wait for the page to load
            time.sleep(3)
            try:
                confirmBtn = driver.find_element(By.NAME, "confirmRegBtn")
                confirmBtn.click()
                time.sleep(3)
                print(f"{i} is done")
            except:
                print(f"{i} is unsucceful")
                unsuccess.append(i)
                continue
        else:
                print(f"{i} is unsucceful")
                unsuccess.append(i)
                continue
    # close the browser
    driver.quit()
    print(f"Total:{i} Done:{i-len(unsuccess)} Failed:{len(unsuccess)}\n Failed Records:{unsuccess}")